/*
 Navicat Premium Data Transfer

 Source Server         : LocalMySQL
 Source Server Type    : MySQL
 Source Server Version : 90001 (9.0.1)
 Source Host           : localhost:3306
 Source Schema         : gongjiaochexinxi

 Target Server Type    : MySQL
 Target Server Version : 90001 (9.0.1)
 File Encoding         : 65001

 Date: 18/12/2024 19:06:02
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for cheliangweizhi
-- ----------------------------
DROP TABLE IF EXISTS `cheliangweizhi`;
CREATE TABLE `cheliangweizhi` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '主键 ',
  `gongjiaoche_id` int DEFAULT NULL COMMENT '车辆',
  `cheliangweizhi_dati` varchar(200) DEFAULT NULL COMMENT '大体位置',
  `cheliangweizhi_fangxiang` varchar(200) DEFAULT NULL COMMENT '行驶方向',
  `cheliangweizhi_mingcheng` varchar(200) DEFAULT NULL COMMENT '下一站名称',
  `cheliangweizhi_content` text COMMENT '路线详情 ',
  `create_time` timestamp NULL DEFAULT NULL COMMENT '创建时间  show1 show2 photoShow',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3 COMMENT='位置信息';

-- ----------------------------
-- Records of cheliangweizhi
-- ----------------------------
BEGIN;
INSERT INTO `cheliangweizhi` (`id`, `gongjiaoche_id`, `cheliangweizhi_dati`, `cheliangweizhi_fangxiang`, `cheliangweizhi_mingcheng`, `cheliangweizhi_content`, `create_time`) VALUES (1, 1, '大体位置1', '行驶方向1', '下一站名称1', '路线详情1', '2022-03-31 19:33:56');
INSERT INTO `cheliangweizhi` (`id`, `gongjiaoche_id`, `cheliangweizhi_dati`, `cheliangweizhi_fangxiang`, `cheliangweizhi_mingcheng`, `cheliangweizhi_content`, `create_time`) VALUES (2, 2, '大体位置2', '行驶方向2', '下一站名称2', '路线详情2', '2022-03-31 19:33:56');
INSERT INTO `cheliangweizhi` (`id`, `gongjiaoche_id`, `cheliangweizhi_dati`, `cheliangweizhi_fangxiang`, `cheliangweizhi_mingcheng`, `cheliangweizhi_content`, `create_time`) VALUES (3, 3, '大体位置3', '行驶方向3', '下一站名称3', '路线详情3', '2022-03-31 19:33:56');
INSERT INTO `cheliangweizhi` (`id`, `gongjiaoche_id`, `cheliangweizhi_dati`, `cheliangweizhi_fangxiang`, `cheliangweizhi_mingcheng`, `cheliangweizhi_content`, `create_time`) VALUES (4, 4, '大体位置4', '行驶方向4', '下一站名称4', '路线详情4', '2022-03-31 19:33:56');
INSERT INTO `cheliangweizhi` (`id`, `gongjiaoche_id`, `cheliangweizhi_dati`, `cheliangweizhi_fangxiang`, `cheliangweizhi_mingcheng`, `cheliangweizhi_content`, `create_time`) VALUES (5, 5, '大体位置5', '行驶方向5', '下一站名称5', '路线详情5', '2022-03-31 19:33:56');
COMMIT;

-- ----------------------------
-- Table structure for config
-- ----------------------------
DROP TABLE IF EXISTS `config`;
CREATE TABLE `config` (
  `id` bigint NOT NULL AUTO_INCREMENT COMMENT '主键',
  `name` varchar(100) NOT NULL COMMENT '配置参数名称',
  `value` varchar(100) DEFAULT NULL COMMENT '配置参数值',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COMMENT='配置文件';

-- ----------------------------
-- Records of config
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for dictionary
-- ----------------------------
DROP TABLE IF EXISTS `dictionary`;
CREATE TABLE `dictionary` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '主键',
  `dic_code` varchar(200) DEFAULT NULL COMMENT '字段',
  `dic_name` varchar(200) DEFAULT NULL COMMENT '字段名',
  `code_index` int DEFAULT NULL COMMENT '编码',
  `index_name` varchar(200) DEFAULT NULL COMMENT '编码名字  Search111 ',
  `super_id` int DEFAULT NULL COMMENT '父字段id',
  `beizhu` varchar(200) DEFAULT NULL COMMENT '备注',
  `create_time` timestamp NULL DEFAULT NULL COMMENT '创建时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb3 COMMENT='字典表';

-- ----------------------------
-- Records of dictionary
-- ----------------------------
BEGIN;
INSERT INTO `dictionary` (`id`, `dic_code`, `dic_name`, `code_index`, `index_name`, `super_id`, `beizhu`, `create_time`) VALUES (1, 'gongjiaoche_types', '车辆类型', 1, '车辆类型1', NULL, NULL, '2022-03-31 19:33:45');
INSERT INTO `dictionary` (`id`, `dic_code`, `dic_name`, `code_index`, `index_name`, `super_id`, `beizhu`, `create_time`) VALUES (2, 'gongjiaoche_types', '车辆类型', 2, '车辆类型2', NULL, NULL, '2022-03-31 19:33:45');
INSERT INTO `dictionary` (`id`, `dic_code`, `dic_name`, `code_index`, `index_name`, `super_id`, `beizhu`, `create_time`) VALUES (3, 'gongjiaoche_types', '车辆类型', 3, '车辆类型3', NULL, NULL, '2022-03-31 19:33:45');
INSERT INTO `dictionary` (`id`, `dic_code`, `dic_name`, `code_index`, `index_name`, `super_id`, `beizhu`, `create_time`) VALUES (4, 'gongjiaoxianlu_types', '线路类型', 1, '线路类型1', NULL, NULL, '2022-03-31 19:33:45');
INSERT INTO `dictionary` (`id`, `dic_code`, `dic_name`, `code_index`, `index_name`, `super_id`, `beizhu`, `create_time`) VALUES (5, 'gongjiaoxianlu_types', '线路类型', 2, '线路类型2', NULL, NULL, '2022-03-31 19:33:45');
INSERT INTO `dictionary` (`id`, `dic_code`, `dic_name`, `code_index`, `index_name`, `super_id`, `beizhu`, `create_time`) VALUES (6, 'gongjiaoxianlu_types', '线路类型', 3, '线路类型3', NULL, NULL, '2022-03-31 19:33:45');
INSERT INTO `dictionary` (`id`, `dic_code`, `dic_name`, `code_index`, `index_name`, `super_id`, `beizhu`, `create_time`) VALUES (7, 'news_types', '公告类型', 1, '公告类型1', NULL, NULL, '2022-03-31 19:33:45');
INSERT INTO `dictionary` (`id`, `dic_code`, `dic_name`, `code_index`, `index_name`, `super_id`, `beizhu`, `create_time`) VALUES (8, 'news_types', '公告类型', 2, '公告类型2', NULL, NULL, '2022-03-31 19:33:45');
INSERT INTO `dictionary` (`id`, `dic_code`, `dic_name`, `code_index`, `index_name`, `super_id`, `beizhu`, `create_time`) VALUES (9, 'news_types', '公告类型', 3, '公告类型3', NULL, NULL, '2022-03-31 19:33:45');
INSERT INTO `dictionary` (`id`, `dic_code`, `dic_name`, `code_index`, `index_name`, `super_id`, `beizhu`, `create_time`) VALUES (10, 'sex_types', '性别类型', 1, '男', NULL, NULL, '2022-03-31 19:33:45');
INSERT INTO `dictionary` (`id`, `dic_code`, `dic_name`, `code_index`, `index_name`, `super_id`, `beizhu`, `create_time`) VALUES (11, 'sex_types', '性别类型', 2, '女', NULL, NULL, '2022-03-31 19:33:45');
COMMIT;

-- ----------------------------
-- Table structure for gongjiaoche
-- ----------------------------
DROP TABLE IF EXISTS `gongjiaoche`;
CREATE TABLE `gongjiaoche` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '主键 ',
  `gongjiaoche_name` varchar(200) DEFAULT NULL COMMENT '车辆编号 Search111 ',
  `gongjiaoche_types` int DEFAULT NULL COMMENT '车辆类型 Search111',
  `gongjiaoche_content` text COMMENT '车辆详情 ',
  `create_time` timestamp NULL DEFAULT NULL COMMENT '创建时间  show1 show2 photoShow',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3 COMMENT='车辆信息';

-- ----------------------------
-- Records of gongjiaoche
-- ----------------------------
BEGIN;
INSERT INTO `gongjiaoche` (`id`, `gongjiaoche_name`, `gongjiaoche_types`, `gongjiaoche_content`, `create_time`) VALUES (1, '车辆编号1', 1, '车辆详情1', '2022-03-31 19:33:56');
INSERT INTO `gongjiaoche` (`id`, `gongjiaoche_name`, `gongjiaoche_types`, `gongjiaoche_content`, `create_time`) VALUES (2, '车辆编号2', 3, '车辆详情2', '2022-03-31 19:33:56');
INSERT INTO `gongjiaoche` (`id`, `gongjiaoche_name`, `gongjiaoche_types`, `gongjiaoche_content`, `create_time`) VALUES (3, '车辆编号3', 2, '车辆详情3', '2022-03-31 19:33:56');
INSERT INTO `gongjiaoche` (`id`, `gongjiaoche_name`, `gongjiaoche_types`, `gongjiaoche_content`, `create_time`) VALUES (4, '车辆编号4', 2, '车辆详情4', '2022-03-31 19:33:56');
INSERT INTO `gongjiaoche` (`id`, `gongjiaoche_name`, `gongjiaoche_types`, `gongjiaoche_content`, `create_time`) VALUES (5, '车辆编号5', 2, '车辆详情5', '2022-03-31 19:33:56');
COMMIT;

-- ----------------------------
-- Table structure for gongjiaoxianlu
-- ----------------------------
DROP TABLE IF EXISTS `gongjiaoxianlu`;
CREATE TABLE `gongjiaoxianlu` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '主键 ',
  `gongjiaoxianlu_name` varchar(200) DEFAULT NULL COMMENT '线路名称 Search111 ',
  `gongjiaoxianlu_types` int DEFAULT NULL COMMENT '线路类型 Search111',
  `gongjiaoxianlu_shijian` varchar(200) DEFAULT NULL COMMENT '发车时间',
  `quancheng` varchar(200) DEFAULT NULL COMMENT '全程',
  `gongjiaoxianlu_numbe` int DEFAULT NULL COMMENT '票价',
  `gongjiaoxianlu_content` text COMMENT '线路详情 ',
  `create_time` timestamp NULL DEFAULT NULL COMMENT '创建时间  show1 show2 photoShow',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3 COMMENT='公交线路';

-- ----------------------------
-- Records of gongjiaoxianlu
-- ----------------------------
BEGIN;
INSERT INTO `gongjiaoxianlu` (`id`, `gongjiaoxianlu_name`, `gongjiaoxianlu_types`, `gongjiaoxianlu_shijian`, `quancheng`, `gongjiaoxianlu_numbe`, `gongjiaoxianlu_content`, `create_time`) VALUES (1, '线路名称1', 3, '发车时间1', '全程1', 483, '线路详情1', '2022-03-31 19:33:56');
INSERT INTO `gongjiaoxianlu` (`id`, `gongjiaoxianlu_name`, `gongjiaoxianlu_types`, `gongjiaoxianlu_shijian`, `quancheng`, `gongjiaoxianlu_numbe`, `gongjiaoxianlu_content`, `create_time`) VALUES (2, '线路名称2', 3, '发车时间2', '全程2', 194, '线路详情2', '2022-03-31 19:33:56');
INSERT INTO `gongjiaoxianlu` (`id`, `gongjiaoxianlu_name`, `gongjiaoxianlu_types`, `gongjiaoxianlu_shijian`, `quancheng`, `gongjiaoxianlu_numbe`, `gongjiaoxianlu_content`, `create_time`) VALUES (3, '线路名称3', 2, '发车时间3', '全程3', 194, '线路详情3', '2022-03-31 19:33:56');
INSERT INTO `gongjiaoxianlu` (`id`, `gongjiaoxianlu_name`, `gongjiaoxianlu_types`, `gongjiaoxianlu_shijian`, `quancheng`, `gongjiaoxianlu_numbe`, `gongjiaoxianlu_content`, `create_time`) VALUES (4, '线路名称4', 3, '发车时间4', '全程4', 387, '线路详情4', '2022-03-31 19:33:56');
INSERT INTO `gongjiaoxianlu` (`id`, `gongjiaoxianlu_name`, `gongjiaoxianlu_types`, `gongjiaoxianlu_shijian`, `quancheng`, `gongjiaoxianlu_numbe`, `gongjiaoxianlu_content`, `create_time`) VALUES (5, '线路名称5', 1, '发车时间5', '全程5', 34, '线路详情5', '2022-03-31 19:33:56');
COMMIT;

-- ----------------------------
-- Table structure for news
-- ----------------------------
DROP TABLE IF EXISTS `news`;
CREATE TABLE `news` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '主键',
  `news_name` varchar(200) DEFAULT NULL COMMENT '公告标题  Search111 ',
  `news_types` int DEFAULT NULL COMMENT '公告类型  Search111 ',
  `news_photo` varchar(200) DEFAULT NULL COMMENT '公告图片',
  `insert_time` timestamp NULL DEFAULT NULL COMMENT '添加时间',
  `news_content` text COMMENT '公告详情',
  `create_time` timestamp NULL DEFAULT NULL COMMENT '创建时间 show1 show2 nameShow',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3 COMMENT='公告信息';

-- ----------------------------
-- Records of news
-- ----------------------------
BEGIN;
INSERT INTO `news` (`id`, `news_name`, `news_types`, `news_photo`, `insert_time`, `news_content`, `create_time`) VALUES (1, '公告标题1', 1, 'http://localhost:8080/gongjiaochexinxi/upload/news1.jpg', '2022-03-31 19:33:56', '公告详情1', '2022-03-31 19:33:56');
INSERT INTO `news` (`id`, `news_name`, `news_types`, `news_photo`, `insert_time`, `news_content`, `create_time`) VALUES (2, '公告标题2', 1, 'http://localhost:8080/gongjiaochexinxi/upload/news2.jpg', '2022-03-31 19:33:56', '公告详情2', '2022-03-31 19:33:56');
INSERT INTO `news` (`id`, `news_name`, `news_types`, `news_photo`, `insert_time`, `news_content`, `create_time`) VALUES (3, '公告标题3', 1, 'http://localhost:8080/gongjiaochexinxi/upload/news3.jpg', '2022-03-31 19:33:56', '公告详情3', '2022-03-31 19:33:56');
INSERT INTO `news` (`id`, `news_name`, `news_types`, `news_photo`, `insert_time`, `news_content`, `create_time`) VALUES (4, '公告标题4', 2, 'http://localhost:8080/gongjiaochexinxi/upload/news4.jpg', '2022-03-31 19:33:56', '公告详情4', '2022-03-31 19:33:56');
INSERT INTO `news` (`id`, `news_name`, `news_types`, `news_photo`, `insert_time`, `news_content`, `create_time`) VALUES (5, '公告标题5', 1, 'http://localhost:8080/gongjiaochexinxi/upload/news5.jpg', '2022-03-31 19:33:56', '公告详情5', '2022-03-31 19:33:56');
COMMIT;

-- ----------------------------
-- Table structure for paiban
-- ----------------------------
DROP TABLE IF EXISTS `paiban`;
CREATE TABLE `paiban` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '主键 ',
  `paiban_name` varchar(200) DEFAULT NULL COMMENT '标题',
  `paiban_a_time` timestamp NULL DEFAULT NULL COMMENT '开始时间',
  `paiban_b_time` timestamp NULL DEFAULT NULL COMMENT '结束时间',
  `siji_id` int DEFAULT NULL COMMENT '司机',
  `paiban_content` text COMMENT '排班详情 ',
  `create_time` timestamp NULL DEFAULT NULL COMMENT '创建时间  show1 show2 photoShow',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb3 COMMENT='排班信息';

-- ----------------------------
-- Records of paiban
-- ----------------------------
BEGIN;
INSERT INTO `paiban` (`id`, `paiban_name`, `paiban_a_time`, `paiban_b_time`, `siji_id`, `paiban_content`, `create_time`) VALUES (1, '标题1', '2022-03-31 19:33:56', '2022-03-31 19:33:56', 1, '排班详情1', '2022-03-31 19:33:56');
INSERT INTO `paiban` (`id`, `paiban_name`, `paiban_a_time`, `paiban_b_time`, `siji_id`, `paiban_content`, `create_time`) VALUES (2, '标题2', '2022-03-31 19:33:56', '2022-03-31 19:33:56', 2, '排班详情2', '2022-03-31 19:33:56');
INSERT INTO `paiban` (`id`, `paiban_name`, `paiban_a_time`, `paiban_b_time`, `siji_id`, `paiban_content`, `create_time`) VALUES (3, '标题3', '2022-03-31 19:33:56', '2022-03-31 19:33:56', 3, '排班详情3', '2022-03-31 19:33:56');
INSERT INTO `paiban` (`id`, `paiban_name`, `paiban_a_time`, `paiban_b_time`, `siji_id`, `paiban_content`, `create_time`) VALUES (4, '标题4', '2022-03-31 19:33:56', '2022-03-31 19:33:56', 4, '排班详情4', '2022-03-31 19:33:56');
INSERT INTO `paiban` (`id`, `paiban_name`, `paiban_a_time`, `paiban_b_time`, `siji_id`, `paiban_content`, `create_time`) VALUES (5, '标题5', '2022-03-31 19:33:56', '2022-03-31 19:33:56', 5, '排班详情5', '2022-03-31 19:33:56');
INSERT INTO `paiban` (`id`, `paiban_name`, `paiban_a_time`, `paiban_b_time`, `siji_id`, `paiban_content`, `create_time`) VALUES (6, '标题6', '2022-05-11 00:00:00', '2022-05-12 00:00:00', 5, '<p>123</p>', '2022-05-20 13:39:07');
COMMIT;

-- ----------------------------
-- Table structure for siji
-- ----------------------------
DROP TABLE IF EXISTS `siji`;
CREATE TABLE `siji` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '主键',
  `siji_uuid_number` varchar(200) DEFAULT NULL COMMENT '工号',
  `siji_name` varchar(200) DEFAULT NULL COMMENT '司机姓名 Search111 ',
  `siji_phone` varchar(200) DEFAULT NULL COMMENT '手机号',
  `siji_number` varchar(200) DEFAULT NULL COMMENT '司机工龄',
  `siji_email` varchar(200) DEFAULT NULL COMMENT '电子邮箱',
  `sex_types` int DEFAULT NULL COMMENT '性别 Search111 ',
  `siji_delete` int DEFAULT '1' COMMENT '假删',
  `create_time` timestamp NULL DEFAULT NULL COMMENT '创建时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3 COMMENT='司机';

-- ----------------------------
-- Records of siji
-- ----------------------------
BEGIN;
INSERT INTO `siji` (`id`, `siji_uuid_number`, `siji_name`, `siji_phone`, `siji_number`, `siji_email`, `sex_types`, `siji_delete`, `create_time`) VALUES (1, '工号1', '司机姓名1', '17703786901', '司机工龄1', '1@qq.com', 2, 1, '2022-03-31 19:33:56');
INSERT INTO `siji` (`id`, `siji_uuid_number`, `siji_name`, `siji_phone`, `siji_number`, `siji_email`, `sex_types`, `siji_delete`, `create_time`) VALUES (2, '工号2', '司机姓名2', '17703786902', '司机工龄2', '2@qq.com', 2, 1, '2022-03-31 19:33:56');
INSERT INTO `siji` (`id`, `siji_uuid_number`, `siji_name`, `siji_phone`, `siji_number`, `siji_email`, `sex_types`, `siji_delete`, `create_time`) VALUES (3, '工号3', '司机姓名3', '17703786903', '司机工龄3', '3@qq.com', 1, 1, '2022-03-31 19:33:56');
INSERT INTO `siji` (`id`, `siji_uuid_number`, `siji_name`, `siji_phone`, `siji_number`, `siji_email`, `sex_types`, `siji_delete`, `create_time`) VALUES (4, '工号4', '司机姓名4', '17703786904', '司机工龄4', '4@qq.com', 1, 1, '2022-03-31 19:33:56');
INSERT INTO `siji` (`id`, `siji_uuid_number`, `siji_name`, `siji_phone`, `siji_number`, `siji_email`, `sex_types`, `siji_delete`, `create_time`) VALUES (5, '工号5', '司机姓名5', '17703786905', '司机工龄5', '5@qq.com', 2, 1, '2022-03-31 19:33:56');
COMMIT;

-- ----------------------------
-- Table structure for token
-- ----------------------------
DROP TABLE IF EXISTS `token`;
CREATE TABLE `token` (
  `id` bigint NOT NULL AUTO_INCREMENT COMMENT '主键',
  `userid` bigint NOT NULL COMMENT '用户id',
  `username` varchar(100) NOT NULL COMMENT '用户名',
  `tablename` varchar(100) DEFAULT NULL COMMENT '表名',
  `role` varchar(100) DEFAULT NULL COMMENT '角色',
  `token` varchar(200) NOT NULL COMMENT '密码',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '新增时间',
  `expiratedtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '过期时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3 COMMENT='token表';

-- ----------------------------
-- Records of token
-- ----------------------------
BEGIN;
INSERT INTO `token` (`id`, `userid`, `username`, `tablename`, `role`, `token`, `addtime`, `expiratedtime`) VALUES (1, 1, 'a1', 'yonghu', '用户', 'vkr3o77v2ahzek3ekrz7td4ow3ox3ifj', '2022-03-31 19:50:11', '2024-12-18 16:31:41');
INSERT INTO `token` (`id`, `userid`, `username`, `tablename`, `role`, `token`, `addtime`, `expiratedtime`) VALUES (2, 1, 'admin', 'users', '管理员', 'zffra3d3as7xxl1vpfp40um0dp5a8y53', '2022-03-31 19:50:36', '2024-12-18 20:03:41');
COMMIT;

-- ----------------------------
-- Table structure for users
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `id` bigint NOT NULL AUTO_INCREMENT COMMENT '主键',
  `username` varchar(100) NOT NULL COMMENT '用户名',
  `password` varchar(100) NOT NULL COMMENT '密码',
  `role` varchar(100) DEFAULT '管理员' COMMENT '角色',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '新增时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3 COMMENT='用户表';

-- ----------------------------
-- Records of users
-- ----------------------------
BEGIN;
INSERT INTO `users` (`id`, `username`, `password`, `role`, `addtime`) VALUES (1, 'admin', 'admin', '管理员', '2022-05-01 00:00:00');
COMMIT;

-- ----------------------------
-- Table structure for yonghu
-- ----------------------------
DROP TABLE IF EXISTS `yonghu`;
CREATE TABLE `yonghu` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '主键',
  `username` varchar(200) DEFAULT NULL COMMENT '账户',
  `password` varchar(200) DEFAULT NULL COMMENT '密码',
  `yonghu_name` varchar(200) DEFAULT NULL COMMENT '用户姓名 Search111 ',
  `yonghu_phone` varchar(200) DEFAULT NULL COMMENT '手机号',
  `yonghu_id_number` varchar(200) DEFAULT NULL COMMENT '身份证号',
  `yonghu_email` varchar(200) DEFAULT NULL COMMENT '电子邮箱',
  `sex_types` int DEFAULT NULL COMMENT '性别 Search111 ',
  `yonghu_delete` int DEFAULT '1' COMMENT '假删',
  `create_time` timestamp NULL DEFAULT NULL COMMENT '创建时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3 COMMENT='用户';

-- ----------------------------
-- Records of yonghu
-- ----------------------------
BEGIN;
INSERT INTO `yonghu` (`id`, `username`, `password`, `yonghu_name`, `yonghu_phone`, `yonghu_id_number`, `yonghu_email`, `sex_types`, `yonghu_delete`, `create_time`) VALUES (1, 'a1', '1', '用户姓名1', '17703786901', '410224199610232001', '1@qq.com', 2, 1, '2022-03-31 19:33:56');
INSERT INTO `yonghu` (`id`, `username`, `password`, `yonghu_name`, `yonghu_phone`, `yonghu_id_number`, `yonghu_email`, `sex_types`, `yonghu_delete`, `create_time`) VALUES (2, 'a2', '123456', '用户姓名2', '17703786902', '410224199610232002', '2@qq.com', 2, 1, '2022-03-31 19:33:56');
INSERT INTO `yonghu` (`id`, `username`, `password`, `yonghu_name`, `yonghu_phone`, `yonghu_id_number`, `yonghu_email`, `sex_types`, `yonghu_delete`, `create_time`) VALUES (3, 'a3', '123456', '用户姓名3', '17703786903', '410224199610232003', '3@qq.com', 1, 1, '2022-03-31 19:33:56');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
