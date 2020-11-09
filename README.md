<h1> Documentation </h1>

<p>The purpose of this project is to read JSON files and create a star scehma data warehouse in postgress database.</br>
Dataset is in the following JSON files.
</p>

<h3>Song dataset format</h3> </br>
<div class="highlight highlight-source-json"><pre>{
  <span class="pl-s"><span class="pl-pds">"</span>num_songs<span class="pl-pds">"</span></span>: <span class="pl-c1">1</span>,
  <span class="pl-s"><span class="pl-pds">"</span>artist_id<span class="pl-pds">"</span></span>: <span class="pl-s"><span class="pl-pds">"</span>ARGSJW91187B9B1D6B<span class="pl-pds">"</span></span>,
  <span class="pl-s"><span class="pl-pds">"</span>artist_latitude<span class="pl-pds">"</span></span>: <span class="pl-c1">35.21962</span>,
  <span class="pl-s"><span class="pl-pds">"</span>artist_longitude<span class="pl-pds">"</span></span>: <span class="pl-c1">-80.01955</span>,
  <span class="pl-s"><span class="pl-pds">"</span>artist_location<span class="pl-pds">"</span></span>: <span class="pl-s"><span class="pl-pds">"</span>North Carolina<span class="pl-pds">"</span></span>,
  <span class="pl-s"><span class="pl-pds">"</span>artist_name<span class="pl-pds">"</span></span>: <span class="pl-s"><span class="pl-pds">"</span>JennyAnyKind<span class="pl-pds">"</span></span>,
  <span class="pl-s"><span class="pl-pds">"</span>song_id<span class="pl-pds">"</span></span>: <span class="pl-s"><span class="pl-pds">"</span>SOQHXMF12AB0182363<span class="pl-pds">"</span></span>,
  <span class="pl-s"><span class="pl-pds">"</span>title<span class="pl-pds">"</span></span>: <span class="pl-s"><span class="pl-pds">"</span>Young Boy Blues<span class="pl-pds">"</span></span>,
  <span class="pl-s"><span class="pl-pds">"</span>duration<span class="pl-pds">"</span></span>: <span class="pl-c1">218.77506</span>,
  <span class="pl-s"><span class="pl-pds">"</span>year<span class="pl-pds">"</span></span>: <span class="pl-c1">0</span>
}</pre></div>

<h3>Song dataset format</h3> </br>

<div class="highlight highlight-source-json"><pre>{
  <span class="pl-s"><span class="pl-pds">"</span>artist<span class="pl-pds">"</span></span>: <span class="pl-s"><span class="pl-pds">"</span>Survivor<span class="pl-pds">"</span></span>,
  <span class="pl-s"><span class="pl-pds">"</span>auth<span class="pl-pds">"</span></span>: <span class="pl-s"><span class="pl-pds">"</span>Logged In<span class="pl-pds">"</span></span>,
  <span class="pl-s"><span class="pl-pds">"</span>firstName<span class="pl-pds">"</span></span>: <span class="pl-s"><span class="pl-pds">"</span>Jayden<span class="pl-pds">"</span></span>,
  <span class="pl-s"><span class="pl-pds">"</span>gender<span class="pl-pds">"</span></span>: <span class="pl-s"><span class="pl-pds">"</span>M<span class="pl-pds">"</span></span>,
  <span class="pl-s"><span class="pl-pds">"</span>itemInSession<span class="pl-pds">"</span></span>: <span class="pl-c1">0</span>,
  <span class="pl-s"><span class="pl-pds">"</span>lastName<span class="pl-pds">"</span></span>: <span class="pl-s"><span class="pl-pds">"</span>Fox<span class="pl-pds">"</span></span>,
  <span class="pl-s"><span class="pl-pds">"</span>length<span class="pl-pds">"</span></span>: <span class="pl-c1">245.36771</span>,
  <span class="pl-s"><span class="pl-pds">"</span>level<span class="pl-pds">"</span></span>: <span class="pl-s"><span class="pl-pds">"</span>free<span class="pl-pds">"</span></span>,
  <span class="pl-s"><span class="pl-pds">"</span>location<span class="pl-pds">"</span></span>: <span class="pl-s"><span class="pl-pds">"</span>New Orleans-Metairie, LA<span class="pl-pds">"</span></span>,
  <span class="pl-s"><span class="pl-pds">"</span>method<span class="pl-pds">"</span></span>: <span class="pl-s"><span class="pl-pds">"</span>PUT<span class="pl-pds">"</span></span>,
  <span class="pl-s"><span class="pl-pds">"</span>page<span class="pl-pds">"</span></span>: <span class="pl-s"><span class="pl-pds">"</span>NextSong<span class="pl-pds">"</span></span>,
  <span class="pl-s"><span class="pl-pds">"</span>registration<span class="pl-pds">"</span></span>: <span class="pl-c1">1541033612796</span>,
  <span class="pl-s"><span class="pl-pds">"</span>sessionId<span class="pl-pds">"</span></span>: <span class="pl-c1">100</span>,
  <span class="pl-s"><span class="pl-pds">"</span>song<span class="pl-pds">"</span></span>: <span class="pl-s"><span class="pl-pds">"</span>Eye Of The Tiger<span class="pl-pds">"</span></span>,
  <span class="pl-s"><span class="pl-pds">"</span>status<span class="pl-pds">"</span></span>: <span class="pl-c1">200</span>,
  <span class="pl-s"><span class="pl-pds">"</span>ts<span class="pl-pds">"</span></span>: <span class="pl-c1">1541110994796</span>,
  <span class="pl-s"><span class="pl-pds">"</span>userAgent<span class="pl-pds">"</span></span>: <span class="pl-s"><span class="pl-pds">"</span><span class="pl-cce">\"</span>Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36<span class="pl-cce">\"</span><span class="pl-pds">"</span></span>,
  <span class="pl-s"><span class="pl-pds">"</span>userId<span class="pl-pds">"</span></span>: <span class="pl-s"><span class="pl-pds">"</span>101<span class="pl-pds">"</span></span>
}</pre></div>

<h3>Entity Relationship Diagram</h3></br>

<img src="/postgress_ERD.png" alt="ERD" style="max-width:100%;">
