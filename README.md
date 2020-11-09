<h1> Documentation </h1>

<p>The purpose of this project is to read JSON files and create a star scehma data warehouse in postgress database.</br>
Dataset is in the following JSON files.
</p>

<h3>Song dataset</h3>
<p>The song dataset contains information about the song and artrist of that song.</br>
The files are partitioned by the first three letters of each song's track ID.</br>
For example, here are filepaths to two files in this dataset.<br>
song_data/A/B/C/TRABCEI128F424C983.json & song_data/A/A/B/TRAABJL12903CDCF1A.json

And below is an example of what a single song file, TRAABJL12903CDCF1A.json, looks like.

</p>

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

Following 2 tables are created from the song data file.

<h4>Songs</h4>
<p>Songs in music database.</p>
<table>
<thead>
<tr>
<th>Column</th>
<th>Type</th>
<th>Nullable</th>
</tr>
</thead>
<tbody>
<tr>
<td>song_id</td>
<td>character varying(18)</td>
<td>not null</td>
</tr>
<tr>
<td>title</td>
<td>character varying</td>
<td>not null</td>
</tr>
<tr>
<td>artist_id</td>
<td>character varying(18)</td>
<td>not null</td>
</tr>
<tr>
<td>year</td>
<td>integer</td>
<td>not null</td>
</tr>
<tr>
<td>duration</td>
<td>double precision</td>
<td>not null</td>
</tr>
</tbody>
</table>
<p>Primary key: song_id</p>
<h4><a id="user-content-artists" class="anchor" aria-hidden="true" href="#artists"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Artists</h4>
<p>Artists in music database.</p>
<table>
<thead>
<tr>
<th>Column</th>
<th>Type</th>
<th>Nullable</th>
</tr>
</thead>
<tbody>
<tr>
<td>artist_id</td>
<td>character varying(18)</td>
<td>not null</td>
</tr>
<tr>
<td>name</td>
<td>character varying</td>
<td>not null</td>
</tr>
<tr>
<td>location</td>
<td>character varying</td>
<td>not null</td>
</tr>
<tr>
<td>latitude</td>
<td>double precision</td>
<td></td>
</tr>
<tr>
<td>longitude</td>
<td>double precision</td>
<td></td>
</tr>
</tbody>
</table>
<p>Primary key: artist_id</p>

<h3>Log dataset</h3> </br>
The log files in the dataset are partitioned by year and month.
For example here are filepaths to two files in this dataset.
log_data/2018/11/2018-11-12-events.json log_data/2018/11/2018-11-13-events.json

And below is an example of what the data in a log file, 2018-11-12-events.json, looks like.

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

From the data log dataset file the following tables are created.

<h4><a id="user-content-time" class="anchor" aria-hidden="true" href="#time"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Time</h4>
<p>Timestamps of records in songplays broken down into specific units.</p>
<table>
<thead>
<tr>
<th>Column</th>
<th>Type</th>
<th>Nullable</th>
</tr>
</thead>
<tbody>
<tr>
<td>start_time</td>
<td>timestamp without time zone</td>
<td>not null</td>
</tr>
<tr>
<td>hour</td>
<td>integer</td>
<td>not null</td>
</tr>
<tr>
<td>day</td>
<td>integer</td>
<td>not null</td>
</tr>
<tr>
<td>week</td>
<td>integer</td>
<td>not null</td>
</tr>
<tr>
<td>month</td>
<td>integer</td>
<td>not null</td>
</tr>
<tr>
<td>year</td>
<td>integer</td>
<td>not null</td>
</tr>
<tr>
<td>weekday</td>
<td>integer</td>
<td>not null</td>
</tr>
</tbody>
</table>

<h4><a id="user-content-users" class="anchor" aria-hidden="true" href="#users"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Users</h4>

<table>
<thead>
<tr>
<th>Column</th>
<th>Type</th>
<th>Nullable</th>
</tr>
</thead><tbody>
<tr>
<td>user_id</td>
<td>integer</td>
<td>not null</td>
</tr>
<tr>
<td>first_name</td>
<td>character varying</td>
<td>not null</td>
</tr>
<tr>
<td>last_name</td>
<td>character varying</td>
<td>not null</td>
</tr>
<tr>
<td>gender</td>
<td>character(1)</td>
<td>not null</td>
</tr>
<tr>
<td>level</td>
<td>character varying</td>
<td>not null</td>
</tr>
</tbody>
</table>
<p>Primary key: user_id</p>

<h3><a id="user-content-songplays" class="anchor" aria-hidden="true" href="#songplays"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Songplays</h3>

<table>
<thead>
<tr>
<th>Column</th>
<th>Type</th>
<th>Nullable</th>
</tr>
</thead>
<tbody>
<tr>
<td>songplay_id</td>
<td>integer</td>
<td>not null</td>
</tr>
<tr>
<td>start_time</td>
<td>timestamp without time zone</td>
<td>not null</td>
</tr>
<tr>
<td>user_id</td>
<td>integer</td>
<td>not null</td>
</tr>
<tr>
<td>level</td>
<td>character varying</td>
<td>not null</td>
</tr>
<tr>
<td>song_id</td>
<td>character varying(18)</td>
<td></td>
</tr>
<tr>
<td>artist_id</td>
<td>character varying(18)</td>
<td></td>
</tr>
<tr>
<td>session_id</td>
<td>integer</td>
<td>not null</td>
</tr>
<tr>
<td>location</td>
<td>character varying</td>
<td>not null</td>
</tr>
<tr>
<td>user_agent</td>
<td>character varying</td>
<td>not null</td>
</tr>
</tbody>
</table>
<p>Primary key: songplay_id</p>

<p>The data in above files is covnerted into the follwoing data model.</p>
<h3>Entity Relationship Diagram</h3>

<img src="/postgress_ERD.png" alt="ERD" style="max-width:100%;">
<hr style="width:50%;text-align:left;margin-left:0">
<h3>ETL Process</h3>
<p> I developed this project using Visual Studio Code, python 3.9.0</br>
installed psycopg2 python driver for PostgreSQL from https://psycopg.org/ </br>
installed pandas from https://pandas.pydata.org/docs/index.html version 1.1.4</br>
installed numpy from https://numpy.org/ version 1.19.3</br>

<code>create_tables.py</code></br>
<code>etl.py</code></br>
<code>sql_queries.py</code></br>

After setting up the environment on my local PC</br>
I first run the script <code>create_tables.py</code> that creates the database and </br>
then run the <code>etl.py</code> to insert the data.
<code>sql_queries.py</code> contains CREATE, DROP and INSERT commands.
