/*
 Navicat MySQL Data Transfer

 Source Server         : localhost
 Source Server Version : 50717
 Source Host           : localhost
 Source Database       : websocket

 Target Server Version : 50717
 File Encoding         : utf-8

 Date: 02/14/2017 21:55:56 PM
*/

SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `alarm`
-- ----------------------------
DROP TABLE IF EXISTS `alarm`;
CREATE TABLE `alarm` (
  `id` tinyint(10) NOT NULL,
  `state` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
--  Records of `alarm`
-- ----------------------------
BEGIN;
INSERT INTO `alarm` VALUES ('1', 'off'), ('2', 'on'), ('3', 'on');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
