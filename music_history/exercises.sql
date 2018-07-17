-- Exercise 01
SELECT genre.label
FROM genre

-- Exercise 02
insert into Artist
values(null, "John Mayer", 1998)

-- Exercise 03
insert into Album
select null, "Continuum", 2006, 4834, "Columbia", artist.artistid, 2
FROM Artist
WHERE Artist.artistname = "John Mayer"

-- Exercise 04
insert into Song
select null, "Gravity", 405, 2006, 3, Artist.artistid, album.albumid
FROM Artist, Album
WHERE Artist.artistname = "John Mayer"
AND album.title = "Continuum"

insert into Song
select null, "Waiting on the World to Change", 405, 2006, 3, Artist.artistid, album.albumid
FROM Artist, Album
WHERE Artist.artistname = "John Mayer"
AND album.title = "Continuum"

insert into Song
select null, "Dreamingg from a Broken Heart", 405, 2006, 3, Artist.artistid, album.albumid
FROM Artist, Album
WHERE Artist.artistname = "John Mayer"
AND album.title = "Continuum"

-- Exercise 05
SELECT al.title, s.title, ar.artistname
FROM Song s
LEFT JOIN album al
ON s.albumid= al.albumid
LEFT JOIN Artist ar
ON ar.artistid = al.artistid
WHERE ar.artistname = "John Mayer"

-- Exercise 06
SELECT count() as "# of songs", album.title
FROM Album 
JOIN Song
ON Song.AlbumId = Album.AlbumId
group by song.albumid

-- Exercise 07
SELECT count() as "# of songs", Artist.artistname
FROM Artist
JOIN Song
ON Song.ArtistId = Artist.ArtistId
group by song.artistid

-- Exercise 08
SELECT count() as "# of songs", Genre.Label
FROM Genre
JOIN Song
ON Song.GenreId = Genre.GenreId
group by song.GenreId

-- Exercise 09
SELECT Album.title, MAX(AlbumLength)
FROM Album

-- Exercise 10
SELECT Song.title, MAX(SongLength)
FROM Song

-- Exercise 11
SELECT Song.title, Album.title, MAX(SongLength)
FROM Song
JOIN Album 
ON Song.AlbumId = album.AlbumId
