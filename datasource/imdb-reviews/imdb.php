<?PHP

function cleanQuery($string)
{
  if(get_magic_quotes_gpc())  // prevents duplicate backslashes
  {
    $string = stripslashes($string);
  }
  if (phpversion() >= '4.3.0')
  {
    $string = mysql_real_escape_string($string);
  }
  else
  {
    $string = mysql_escape_string($string);
  }
  return $string;
}



   $link=mysql_connect('localhost','root','');
   if (!$link)
   {  
      return false;
   } 
   $select=mysql_select_db('imdb_reviews',$link);
   if (!$select)
   {
      echo mysql_error();
   }


function getNodeInnerHTML($elem) { 

   return simplexml_import_dom($elem)->asXML(); 

} 
  
  
$urls = array(
	'http://www.imdb.com/title/tt0120338/usercomments' => 2271,
	'http://www.imdb.com/title/tt1073498/usercomments' => 389,
	'http://www.imdb.com/title/tt0068646/usercomments' => 1457,
	'http://www.imdb.com/title/tt1285016/usercomments' => 377,
	'http://www.imdb.com/title/tt0099674/usercomments' => 459,
	'http://www.imdb.com/title/tt0111161/usercomments' => 2327,
	'http://www.imdb.com/title/tt0499549/usercomments' => 2728
);

  

$oldSetting = libxml_use_internal_errors( true ); 
libxml_clear_errors(); 

 
foreach($urls as $url_to_load => $max_items){
	echo '<br/>URL: '.$url_to_load.' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++'.$max_items.' </br></br>';
	  
	$iterator = 0;
	//$max_items = 10; //useful if I can actually manage and get the number of reviews from the page; which I haven't just yet

	
	//continue; //comment to enable the crawler
	
	while ($iterator<$max_items){

		$html = new DOMDocument(); 
		$html->loadHtmlFile($url_to_load.'?start='.$iterator); 
		
		//get the actual number of reviews the first run in...
		/*
		if($iterator==0){ //let's actually get a count of the number of reviews
			$xpath = new DOMXPath( $html ); 
			$count = $xpath->query( "/html/body[@id='styleguide-v2']/div[@id='wrapper']/div[@id='root']/layer/div[@id='pagecontent']/div[@id='tn15']/div[@id='tn15main']/div[@id='tn15content']/table[2]/tbody/tr/td[2]"); 
			foreach ( $count as $countvar ) {	
				echo 'gagaaaa';
				echo 'TOTAL: '.$countvar->nodeValue.'<<';//->nodeValue;
				}
		}
		*/
		 
		$xpath = new DOMXPath( $html ); 
		$links = $xpath->query( "/html/body[@id='styleguide-v2']/div[@id='wrapper']/div[@id='root']/layer/div[@id='pagecontent']/div[@id='tn15']/div[@id='tn15main']/div[@id='tn15content']/p" ); 
		 
		//$return = array();

		$_rating = -1;
		foreach ( $links as $item ) {
			if($item->nodeValue=='*** This review may contain spoilers ***') continue; //skip over spoilers ;)
			
			$ratingitem = $item->getElementsByTagName('small')->item(0);
			if ($ratingitem instanceof DOMElement){ //rating is given here
				
				$ratingitem = $item->getElementsByTagName('img')->item(0); //extract from alt tag
				if ($ratingitem instanceof DOMElement){
					$_rating = $ratingitem->getAttribute('alt');
					$rating_int = (int)substr($_rating,0,strpos($_rating,'/'));
				}
				
				
			}else{ //this is the actual review
				if($_rating==-1){
					//echo 'NOOOO RATING :((('; 
					continue;
				}
				//echo '<br/><br/><br/>======================'.$_rating.'=====================<br/>'.$item->nodeValue;
				
				$sql = "INSERT INTO reviews(review,rating,url) VALUES('".cleanQuery($item->nodeValue)."',".$rating_int.",'".cleanQuery($url_to_load.'?start='.$iterator)."');";
				$result = mysql_query($sql);
				//die(); //test mode
				
				$_rating = -1;
			}
			/*
			echo '<br/>======================<br/>'.$item->nodeValue;
			print_r(getNodeInnerHTML($item));
			$ratingitem = $item->getElementsByTagName('img')->item(0);
			if ($ratingitem instanceof DOMElement)
			echo '::'.$ratingitem->getAttribute('alt').'<<';
			//$rating = $ratingitem->getAttribute('alt');
			//echo $rating;
			*/
		}

		$iterator += 10;
		sleep(1.5);
		
	}
}
 
libxml_clear_errors(); 
libxml_use_internal_errors( $oldSetting ); 

?>