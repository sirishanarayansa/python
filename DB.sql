#create database Blog;
#Use Blog;
#show tables;
#Create table Users(UserId varchar(50) primary key, Username varchar(50), email varchar(50) unique key)

#create table blog_post ( blogid int primary key, 
#blog_title varchar (200) not null, 
#contents varchar (1000) not null,
#userid varchar (30) references users(userid),
#posting_date timestamp default current_timestamp not null)

#Create table blog_comments(
#comment_id int primary key,
#comment_text varchar (200) not null,
#blogid int references blog_post(blogid),
#userid varchar (30) references users(userid),
#comment_date timestamp default current_timestamp not null
#)

#show tables
#INSERT INTO Users VALUES (101, 'John','john1@gmail.com')
#INSERT INTO Users VALUES (102, 'Alex','alex2@gmail.com')
#INSERT INTO Users VALUES (103, 'Chris','chris3@gmail.com')

#INSERT INTO blog_post Values (1001,'Best Solution Ever','ABC', 102)
#Desc Blog_post
#INSERT INTO blog_post (blogid, blog_title, contents, userid) VALUES (1001,'Atomic Habits', 'ABC', 102)
#INSERT INTO blog_post (blogid, blog_title, contents, userid) VALUES (1002,'Path of Perfection', 'XYZ', 101)
#INSERT INTO blog_post (blogid, blog_title, contents, userid) VALUES (1003,'Blue place', 'XYX', 103)

#INSERT INTO blog_comments (comment_id, comment_text, blogid, userid) VALUES (001,'Life changing book', '1001', 102)
#INSERT INTO blog_comments (comment_id, comment_text, blogid, userid) VALUES (002,'Spirituality', '1002', 101)
#INSERT INTO blog_comments (comment_id, comment_text, blogid, userid) VALUES (003,'Mesmerising for eyes', '1003', 103)

 DESC Users;
 Select * from Users;
 select * from blog_post;
 Select * from blog_comments;
 
 #select Users.username, Users.email, blog_post.Contents, blog_post.blogid, blog_post.blog_title, blog_post.contents From Users Inner Join blog_post on Users.UserId = blog_post.userid
 #INSERT INTO blog_comments (comment_id, comment_text, blogid, userid) VALUES (004,'Huge conetnt but everysone should read this blog once in his lifetime', '1001', 102) 
 select * from blog_post ORDER BY blog_title DESC;
 #select * from blog_post ORDER BY posting_date ASC;

 