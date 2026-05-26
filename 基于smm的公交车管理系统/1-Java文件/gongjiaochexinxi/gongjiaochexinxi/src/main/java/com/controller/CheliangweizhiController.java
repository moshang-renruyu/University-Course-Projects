
package com.controller;

import java.io.File;
import java.math.BigDecimal;
import java.net.URL;// 导入URL类
import java.text.SimpleDateFormat;// 导入日期格式化类
import com.alibaba.fastjson.JSONObject;
import java.util.*;// 导入Java工具包
import org.springframework.beans.BeanUtils;// 导入Spring Bean工具类
import javax.servlet.http.HttpServletRequest;// 导入HttpServletRequest接口
import org.springframework.web.context.ContextLoader;// 导入Spring ContextLoader
import javax.servlet.ServletContext;// 导入ServletContext接口
import com.service.TokenService;// 导入TokenService服务
import com.utils.*; // 导入com.utils包下的工具类
import java.lang.reflect.InvocationTargetException;// 导入反射相关的异常类

import com.service.DictionaryService;// 导入DictionaryService服务
import org.apache.commons.lang3.StringUtils;// 导入Apache Commons Lang StringUtils类
import com.annotation.IgnoreAuth;// 导入自定义的注解IgnoreAuth
import org.slf4j.Logger;// 导入日志Logger接口
import org.slf4j.LoggerFactory; // 导入日志LoggerFactory类
import org.springframework.beans.factory.annotation.Autowired;// 导入Spring的Autowired注解
import org.springframework.stereotype.Controller;// 导入Spring的Controller注解
import org.springframework.web.bind.annotation.*;// 导入Spring的Web绑定注解
import com.baomidou.mybatisplus.mapper.EntityWrapper; // 导入MyBatis Plus的EntityWrapper类
import com.baomidou.mybatisplus.mapper.Wrapper;// 导入MyBatis Plus的Wrapper接口
import com.entity.*;// 导入com.entity包下的实体类
import com.entity.view.*;// 导入com.entity.view包下视图类
import com.service.*;// 导入com.service包下的服务类
import com.utils.PageUtils;// 导入PageUtils工具类
import com.utils.R;// 导入R工具类
import com.alibaba.fastjson.*;// 导入FastJSON包下的工具类

/**
 * 位置信息
 * 后端接口
 * @author
 * @email
*/
@RestController// 声明这是一个REST控制器
@Controller// 声明这是一个Spring MVC控制器
@RequestMapping("/cheliangweizhi")// 定义类级别的请求映射路径
public class CheliangweizhiController {
    private static final Logger logger = LoggerFactory.getLogger(CheliangweizhiController.class);
    // 创建日志对象
    @Autowired// 自动注入CheliangweizhiService服务
    private CheliangweizhiService cheliangweizhiService;


    @Autowired
    private TokenService tokenService;
    @Autowired
    private DictionaryService dictionaryService;

    //级联表service
    @Autowired
    private GongjiaocheService gongjiaocheService;

    @Autowired
    private YonghuService yonghuService;


    /**
     * 后端列表
     */
    @RequestMapping("/page")// 定义方法级别的请求映射路径
    public R page(@RequestParam Map<String, Object> params, HttpServletRequest request) {//方法参数使用@RequestParam注解来接收客户端发送的所有请求参数，并将其存储在一个Map<String, Object>中。同时，它还接收一个HttpServletRequest对象，这个对象包含了原生的HTTP请求信息。
        logger.debug("page方法:,,Controller:{},,params:{}", this.getClass().getName(), JSONObject.toJSONString(params));// 记录日志
        String role = String.valueOf(request.getSession().getAttribute("role"));
        // 从session中获取角色
        if (false) // 一个永远不会执行的条件
            return R.error(511, "永不会进入");
        else if ("用户".equals(role))// 如果角色是用户
            params.put("yonghuId", request.getSession().getAttribute("userId"));// 添加用户ID到参数
        if (params.get("orderBy") == null || params.get("orderBy") == "") {// 如果没有指定排序字段
            params.put("orderBy", "id");// 默认按ID排序
        }
        PageUtils page = cheliangweizhiService.queryPage(params);// 调用服务查询分页数据


        //字典表数据转换
        List<CheliangweizhiView> list = (List<CheliangweizhiView>) page.getList();// 获取分页数据列表
        for (CheliangweizhiView c : list) {// 遍历列表
            //修改对应字典表字段
            dictionaryService.dictionaryConvert(c, request); // 调用字典服务进行数据转换
        }
        return R.ok().put("data", page);// 返回分页数据
    }

    /**
     * 后端详情
     */
    @RequestMapping("/info/{id}")// 定义方法级别的请求映射路径，包含{id}作为路径变量
    public R info(@PathVariable("id") Long id, HttpServletRequest request) {
        logger.debug("info方法:,,Controller:{},,id:{}", this.getClass().getName(), id);// 记录日志
        CheliangweizhiEntity cheliangweizhi = cheliangweizhiService.selectById(id);// 根据ID查询实体
        if (cheliangweizhi != null) {// 如果实体不为空
            //entity转view
            CheliangweizhiView view = new CheliangweizhiView(); // 创建视图对象
            BeanUtils.copyProperties(cheliangweizhi, view);//把实体数据重构到view中

            //级联表
            GongjiaocheEntity gongjiaoche = gongjiaocheService.selectById(cheliangweizhi.getGongjiaocheId());// 根据车辆ID查询级联表实体
            if (gongjiaoche != null) {
                BeanUtils.copyProperties(gongjiaoche, view, new String[]{"id", "createTime", "insertTime", "updateTime"});//把级联的数据添加到view中,并排除id和创建时间字段
                view.setGongjiaocheId(gongjiaoche.getId()); // 设置车辆ID
            }
            //修改对应字典表字段
            dictionaryService.dictionaryConvert(view, request); // 调用字典服务进行数据转换
            return R.ok().put("data", view);// 返回视图对象
        } else {
            return R.error(511, "查不到数据");// 如果实体为空，返回错误信息
        }

    }

    /**
     * 后端保存
     */
    @RequestMapping("/save")// 定义方法级别的请求映射路径
    public R save(@RequestBody CheliangweizhiEntity cheliangweizhi, HttpServletRequest request) {
        logger.debug("save方法:,,Controller:{},,cheliangweizhi:{}", this.getClass().getName(), cheliangweizhi.toString());// 记录日志

        String role = String.valueOf(request.getSession().getAttribute("role"));// 从session中获取角色
        if (false)
            return R.error(511, "永远不会进入");

        Wrapper<CheliangweizhiEntity> queryWrapper = new EntityWrapper<CheliangweizhiEntity>()
                .eq("gongjiaoche_id", cheliangweizhi.getGongjiaocheId())// 根据车辆ID查询
                .eq("cheliangweizhi_dati", cheliangweizhi.getCheliangweizhiDati())
                .eq("cheliangweizhi_fangxiang", cheliangweizhi.getCheliangweizhiFangxiang())
                .eq("cheliangweizhi_mingcheng", cheliangweizhi.getCheliangweizhiMingcheng());

        logger.info("sql语句:" + queryWrapper.getSqlSegment());// 记录SQL语句
        CheliangweizhiEntity cheliangweizhiEntity = cheliangweizhiService.selectOne(queryWrapper); // 调用服务查询实体
        if (cheliangweizhiEntity == null) {// 如果实体为空
            cheliangweizhi.setCreateTime(new Date());// 设置创建时间
            cheliangweizhiService.insert(cheliangweizhi);// 插入实体
            return R.ok();// 返回成功信息
        } else {
            return R.error(511, "表中有相同数据");// 如果实体不为空，返回错误信息
        }
    }

    /**
     * 后端修改
     */
    @RequestMapping("/update")// 定义方法级别的请求映射路径
    public R update(@RequestBody CheliangweizhiEntity cheliangweizhi, HttpServletRequest request) {
        logger.debug("update方法:,,Controller:{},,cheliangweizhi:{}", this.getClass().getName(), cheliangweizhi.toString());
// 记录调试信息，包括类名和传入的cheliangweizhi对象的字符串表示
        String role = String.valueOf(request.getSession().getAttribute("role"));// 从请求的session中获取角色信息
//        if(false)
//            return R.error(511,"永远不会进入");
        //根据字段查询是否有相同数据
        Wrapper<CheliangweizhiEntity> queryWrapper = new EntityWrapper<CheliangweizhiEntity>()
                .notIn("id", cheliangweizhi.getId())// 排除当前id
                .andNew()// 开启新的查询条件
                .eq("gongjiaoche_id", cheliangweizhi.getGongjiaocheId())// 等于车辆id
                .eq("cheliangweizhi_dati", cheliangweizhi.getCheliangweizhiDati())
                .eq("cheliangweizhi_fangxiang", cheliangweizhi.getCheliangweizhiFangxiang())
                .eq("cheliangweizhi_mingcheng", cheliangweizhi.getCheliangweizhiMingcheng());

        logger.info("sql语句:" + queryWrapper.getSqlSegment()); // 记录实际执行的SQL语句
        CheliangweizhiEntity cheliangweizhiEntity = cheliangweizhiService.selectOne(queryWrapper);// 执行查询
        if (cheliangweizhiEntity == null) {// 如果没有查到相同数据
            cheliangweizhiService.updateById(cheliangweizhi);//根据id更新
            return R.ok(); // 返回成功响应
        } else {
            return R.error(511, "表中有相同数据");// 如果查到相同数据，返回错误响应
        }
    }

    /**
     * 删除
     */
    @RequestMapping("/delete")// 定义方法级别的请求映射路径为 "/delete"
    public R delete(@RequestBody Integer[] ids) {// 使用RequestBody注解接收请求体中的ids数组
        logger.debug("delete:,,Controller:{},,ids:{}", this.getClass().getName(), ids.toString());// 记录调试信息
        cheliangweizhiService.deleteBatchIds(Arrays.asList(ids));
        return R.ok();
    }


    /**
     * 批量上传
     */
    @RequestMapping("/batchInsert")// 定义方法级别的请求映射路径为 "/batchInsert"
    public R save(String fileName, HttpServletRequest request) {// 接收文件名和HTTP请求对象
        logger.debug("batchInsert方法:,,Controller:{},,fileName:{}", this.getClass().getName(), fileName);// 记录调试信息
        Integer yonghuId = Integer.valueOf(String.valueOf(request.getSession().getAttribute("userId")));// 从session中获取用户ID
        SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");// 创建日期格式化对象
        try {
            List<CheliangweizhiEntity> cheliangweizhiList = new ArrayList<>();//上传的东西
            Map<String, List<String>> seachFields = new HashMap<>();//要查询的字段
            Date date = new Date(); // 创建当前日期对象
            int lastIndexOf = fileName.lastIndexOf(".");// 查找文件名中最后一个点的位置
            if (lastIndexOf == -1) {// 如果没有找到点，即没有后缀
                return R.error(511, "该文件没有后缀");// 返回错误响应
            } else {
                String suffix = fileName.substring(lastIndexOf);// 获取文件后缀
                if (!".xls".equals(suffix)) {// 如果后缀不是.xls
                    return R.error(511, "只支持后缀为xls的excel文件"); // 返回错误响应
                } else {
                    URL resource = this.getClass().getClassLoader().getResource("../../upload/" + fileName);//获取文件路径
                    File file = new File(resource.getFile());// 创建文件对象
                    if (!file.exists()) { // 如果文件不存在
                        return R.error(511, "找不到上传文，请联系管理员");// 返回错误响应
                    } else {
                        List<List<String>> dataList = PoiUtil.poiImport(file.getPath());//读取xls文件
                        dataList.remove(0);//删除第一行，因为第一行是提示
                        for (List<String> data : dataList) {
                            //循环,遍历数据行
                            CheliangweizhiEntity cheliangweizhiEntity = new CheliangweizhiEntity();
//                            cheliangweizhiEntity.setGongjiaocheId(Integer.valueOf(data.get(0)));   //车辆 要改的
//                            cheliangweizhiEntity.setCheliangweizhiDati(data.get(0));                    //大体位置 要改的
//                            cheliangweizhiEntity.setCheliangweizhiFangxiang(data.get(0));                    //行驶方向 要改的
//                            cheliangweizhiEntity.setCheliangweizhiMingcheng(data.get(0));                    //下一站名称 要改的
//                            cheliangweizhiEntity.setCheliangweizhiContent("");//详情和图片
//                            cheliangweizhiEntity.setCreateTime(date);//时间
                            cheliangweizhiList.add(cheliangweizhiEntity);


                            //把要查询是否重复的字段放入map中
                        }

                        //查询是否重复
                        cheliangweizhiService.insertBatch(cheliangweizhiList);// 批量插入数据
                        return R.ok();// 返回成功响应
                    }
                }
            }
        } catch (Exception e) {
            e.printStackTrace(); // 打印异常堆栈
            return R.error(511, "批量插入数据异常，请联系管理员");// 返回错误响应
        }
    }
}