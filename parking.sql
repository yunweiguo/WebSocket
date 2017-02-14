/*
 Navicat MySQL Data Transfer

 Source Server         : localhost
 Source Server Version : 50717
 Source Host           : localhost
 Source Database       : websocket

 Target Server Version : 50717
 File Encoding         : utf-8

 Date: 02/14/2017 21:56:04 PM
*/

SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `parking`
-- ----------------------------
DROP TABLE IF EXISTS `parking`;
CREATE TABLE `parking` (
  `id` tinyint(4) NOT NULL,
  `state` varchar(10) NOT NULL,
  `start_time` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
--  Records of `parking`
-- ----------------------------
BEGIN;
INSERT INTO `parking` VALUES ('1', 'busy', '02-14 20:23:37'), ('2', 'available', '/');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
