/*
SQLyog Community v13.1.5  (64 bit)
MySQL - 5.6.12-log : Database - matrimony
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`matrimony` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `matrimony`;

/*Table structure for table `answers` */

DROP TABLE IF EXISTS `answers`;

CREATE TABLE `answers` (
  `ans_id` int(11) NOT NULL AUTO_INCREMENT,
  `extraversion` varchar(20) DEFAULT NULL,
  `agreeableness` varchar(20) DEFAULT NULL,
  `conscientious` varchar(20) DEFAULT NULL,
  `neuroticism` varchar(20) DEFAULT NULL,
  `openness` varchar(20) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `result` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`ans_id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=latin1;

/*Data for the table `answers` */

insert  into `answers`(`ans_id`,`extraversion`,`agreeableness`,`conscientious`,`neuroticism`,`openness`,`user_id`,`result`) values 
(1,'10','15','15','10','12',2,'serious'),
(2,'10','20','13','8','16',3,'extraverted'),
(3,'10','16','14','12','14',4,'extraverted'),
(4,'15','10','9','9','12',6,'serious'),
(5,'20','13','12','13','17',7,'dependable'),
(6,'7','13','13','12','15',8,'serious'),
(7,'12','12','12','12','12',9,'serious'),
(8,'12','12','12','12','12',10,'extraverted'),
(9,'12','12','12','12','12',11,'extraverted'),
(10,'4','20','12','4','20',12,'serious'),
(11,'15','16','13','9','17',13,'dependable'),
(12,'14','12','11','6','11',14,'serious'),
(13,'9','12','12','13','12',5,'serious'),
(14,'10','10','10','14','12',15,'serious'),
(15,'11','12','11','11','11',20,'serious'),
(16,'11','12','11','11','11',20,'serious'),
(17,'11','12','11','11','11',20,'serious'),
(18,'11','12','11','11','11',20,'serious'),
(19,'11','12','11','11','11',20,'serious'),
(20,'12','11','10','11','12',21,'serious'),
(21,'10','14','15','13','12',23,'extraverted'),
(22,'10','14','12','12','13',25,'extraverted'),
(23,'13','14','14','15','19',26,'dependable');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(50) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL,
  `user_type` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`user_name`,`password`,`user_type`) values 
(1,'admin','admin','admin'),
(2,'joe@gmail.com','12345','user'),
(3,'arun@gmail.com','12345','user'),
(4,'jyothika@gmail.com','12345','user'),
(5,'riya@gmail.com','12345','user'),
(6,'anil@gmail.com','12345','user'),
(7,'aysha@gmail.com','aysha','user'),
(8,'anwar@gmail.com','anwar','user'),
(9,'ajay@gmail.com','ajay','user'),
(10,'rama@gmail.com','rama','user'),
(11,'navmi@gmail.com','navmi','user'),
(12,'arjun@gmail.com','12345','user'),
(13,'sid@gmail.com','1234','user'),
(14,'jeru.mb@gmail.com','1234','user'),
(15,'akhil@gmail.com','12345','user'),
(20,'david@gmail.com','12345','user'),
(21,'liya@gmail.com','12345','user'),
(22,'easther@gmail.com','12345','user'),
(23,'riya2@gmail.com','12345','user'),
(24,'aleena@gmail.com','12345','user'),
(25,'rema@gmail.com','12345','user'),
(26,'jesliyapv@gmail.com','12345','user'),
(27,'radhika@gmail.com','12345','pending');

/*Table structure for table `matching` */

DROP TABLE IF EXISTS `matching`;

CREATE TABLE `matching` (
  `match_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `r_id` int(11) DEFAULT NULL,
  `score` float DEFAULT NULL,
  PRIMARY KEY (`match_id`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=latin1;

/*Data for the table `matching` */

insert  into `matching`(`match_id`,`user_id`,`r_id`,`score`) values 
(1,4,3,98.1636),
(2,6,4,94.9036),
(3,4,6,94.9036),
(4,8,7,93.1032),
(5,9,4,98.8272),
(6,10,3,95.2778),
(7,10,6,97.9181),
(8,10,9,100),
(9,11,3,95.2778),
(10,11,6,97.9181),
(11,11,9,100),
(12,4,9,98.8272),
(13,12,4,91.7416),
(14,12,10,85.8897),
(15,12,11,85.8897),
(16,13,7,97.9051),
(17,9,10,100),
(18,9,11,100),
(19,10,12,85.8897),
(20,5,2,98.3866),
(21,5,14,94.2682),
(22,15,4,97.4104),
(23,15,10,98.9949),
(24,15,11,98.9949),
(25,20,21,99.6822),
(26,21,20,99.6822),
(27,3,4,98.1636),
(28,3,10,95.2778),
(29,3,11,95.2778),
(30,5,20,99.3211),
(31,20,23,99.2114),
(32,23,20,99.2114),
(33,25,20,99.6124),
(34,2,5,98.3866),
(35,2,21,97.4179),
(36,2,23,99.4158),
(37,2,25,99.0652),
(38,20,25,99.6124);

/*Table structure for table `preference` */

DROP TABLE IF EXISTS `preference`;

CREATE TABLE `preference` (
  `p_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `u_id` bigint(20) DEFAULT NULL,
  `family_status` varchar(20) DEFAULT NULL,
  `education` varchar(20) DEFAULT NULL,
  `age_max` int(11) DEFAULT NULL,
  `age_min` int(11) DEFAULT NULL,
  PRIMARY KEY (`p_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `preference` */

insert  into `preference`(`p_id`,`u_id`,`family_status`,`education`,`age_max`,`age_min`) values 
(1,20,'below average','post graduation',26,20),
(2,21,'average','post graduation',30,23),
(3,22,'average','post graduation',27,22),
(4,23,'average','post graduation',27,23),
(5,24,'average','graduation',27,22),
(6,25,'average','post graduation',26,23),
(7,26,'average','post graduation',29,27),
(8,27,'average','graduation',30,23);

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `user_id` int(11) DEFAULT NULL,
  `uname` varchar(30) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  `phone_no` bigint(10) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `occupation` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `religion` varchar(30) NOT NULL,
  `post` varchar(30) DEFAULT NULL,
  `pin` bigint(20) DEFAULT NULL,
  `qualification` varchar(30) DEFAULT NULL,
  `family_status` varchar(40) DEFAULT NULL,
  `height` bigint(20) DEFAULT NULL,
  `weight` bigint(20) DEFAULT NULL,
  `complexion` varchar(30) DEFAULT NULL,
  `body_type` varchar(30) DEFAULT NULL,
  `gender` varchar(30) DEFAULT NULL,
  `photo` varchar(100) DEFAULT NULL,
  `edu_level` varchar(100) DEFAULT NULL,
  `caste` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`user_id`,`uname`,`email`,`phone_no`,`dob`,`age`,`occupation`,`place`,`religion`,`post`,`pin`,`qualification`,`family_status`,`height`,`weight`,`complexion`,`body_type`,`gender`,`photo`,`edu_level`,`caste`) values 
(2,'joe','joe@gmail.com',7025609763,'1997-06-04',25,'doctor','Kunnamkulam','Christian','Chowannur',680517,'mbbs','middle class',6,60,'fair','slim','Male','/static/220428-080200.jpg','post graduation','rc'),
(3,'arun','arun@gmail.com',7025609763,'1997-06-04',25,'nurse','Kunnamkulam','Hindu','Chowannur',680517,'bsc','middle class',6,63,'wheetish','slim','Male','/static/220428-081140.jpg','nurse','thiyya'),
(4,'jyothika','jyothika@gmail.com',7894567345,'1999-07-08',23,'System Engineer','thrissur','Hindu','thrissur',679576,'MCA','middle class',6,60,'fair','lean','Female','/static/220428-081430.jpg','engineer','thiyya'),
(5,'riya','riya@gmail.com',7025609763,'1997-07-10',23,'singer','Kunnamkulam','Christian','thrissur',680517,'ma','middle class',6,60,'fair','slim','Female','/static/220428-081622.jpg','artist','rc'),
(6,'anil','anil@gmail.com',7025609763,'1997-07-10',25,'teacher','thrissur','Hindu','Chowannur',680517,'ma','middle class',6,60,'brownish','slim','Male','/static/220428-082831.jpg','teacher','thiyya'),
(7,'aysha','aysha@gmail.com',7894567345,'2000-07-10',22,'Youtuber','thrissur','Muslim','thrissur',679576,'BBA','Middle Class',5,60,'fair','slim','Female','/static/220428-083500.jpg','youtuber','ISLAM'),
(8,'Anwar','anwar@gmail.com',7025609769,'1995-12-27',27,'Youtuber','thrissur','Muslim','thrissur',680517,'btech','Middle Class',6,75,'fair','slim','Male','/static/220428-083733.jpg','youtuber','ISLAM'),
(9,'Ajay','ajay@gmail.com',7894567345,'1997-05-07',25,'Clerk','thrissur','Hindu','thrissur',679576,'bsc','middle class',6,75,'brownish','slim','Male','/static/220428-084509.jpg','teacher','thiyya'),
(10,'rama','bincykb998@gmail.com',7025609768,'1995-02-21',23,'teacher','Kunnamkulam','Hindu','thrissur',680517,'bsc','Middle Class',5,60,'wheetish','slim','Female','/static/220428-084849.jpg','teacher','thiyya'),
(11,'Navmi','navmi@gmail.com',7894567345,'2000-06-05',22,'doctor','thrissur','Hindu','thrissur',679576,'mbbs','Middle Class',5,63,'fair','lean','Female','/static/220428-085603.jpg','doctor','thiyya'),
(12,'arjun','arjun@gmail.com',7894567345,'1997-10-15',25,'doctor','thrissur','Hindu','thrissur',679576,'mbbs','middle class',6,60,'wheetish','slim','Male','/static/220428-094013.jpg','doctor','thiyya'),
(13,'sid','sid@gmail.com',7025609763,'1997-10-10',24,'engineer','thrissur','Muslim','thrissur',680517,'MCA','middle class',6,84,'brownish','normal','Male','/static/220428-140233.jpg','post graduation','ISLAM'),
(14,'jerin mb','jeru.mb@gmail.com',7894567345,'1996-10-18',26,'politician','thrissur','Christian','thrissur',679576,'NIL','very rich',6,100,'fair','chubby','Male','/static/220428-141332.jpg','educated','rc'),
(15,'akhil','akhil@gmail.com',7025609763,'1994-11-17',27,'teacher','thrissur','Hindu','thrissur',680517,'bsc','middle class',6,60,'wheetish','slim','Male','/static/220428-153146.jpg','teacher','thiyya'),
(20,'david','david@gmail.com',7025609763,'1996-06-05',26,'teacher','thrissur','Christian','thrissur',680517,'ma','average',6,75,'fair','lean','Male','/static/220430-192528.jpg','post graduation','rc'),
(21,'liya','liya@gmail.com',7025609763,'1998-08-04',23,'teacher','thrissur','Christian','thrissur',680517,'ma','above Average ',5,63,'fair','slim','Female','/static/220504-091115.jpg','post graduation','rc'),
(22,'easther','easther@gmail.com',7025609763,'1998-05-20',23,'teacher','thrissur','Christian','thrissur',680517,'ma','average',5,63,'fair','slim','Female','/static/220505-094952.jpg','post graduation','rc'),
(23,'riya','riya2@gmail.com',7025609763,'1998-05-26',23,'teacher','thrissur','Christian','thrissur',680517,'ma','average',6,63,'fair','slim','Female','/static/220505-110513.jpg','post graduation','rc'),
(24,'aleena','aleena@gmail.com',7025609763,'2000-05-05',22,'System Engineer','thrissur','Christian','thrissur',680517,'MCA','average',6,63,'fair','slim','Female','/static/220505-114408.jpg','post graduation','rc'),
(25,'rema','rema@gmail.com',7025609763,'1999-05-11',23,'teacher','thrissur','Christian','thrissur',680517,'ma','average',5,63,'fair','slim','Female','/static/220505-133310.jpg','post graduation','rc'),
(26,'jesliya','jesliyapv@gmail.com',9675546789,'1998-06-30',23,'System Engineer','edappal','Muslim','edappal',679576,'MCA','average',5,56,'brownish','slim','Female','/static/220506-141427.jpg','post graduation','ISLAM'),
(27,'radhika','radhika@gmail.com',7025609763,'1998-05-06',23,'nurse','thrissur','Hindu','thrissur',680517,'bsc','average',5,63,'fair','slim','Female','/static/220510-174117.jpg','graduation','thiyya');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
