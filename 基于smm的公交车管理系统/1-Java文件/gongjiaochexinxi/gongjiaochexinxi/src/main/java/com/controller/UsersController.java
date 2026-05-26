
package com.controller;


import java.util.Arrays;// 导入数组工具类
import java.util.Map;// 导入Map接口
import javax.servlet.http.HttpServletRequest;// 导入HttpServletRequest接口

import com.service.UsersService; // 导入UsersService服务
import org.springframework.beans.factory.annotation.Autowired;// 导入Spring的Autowired注解
import org.springframework.web.bind.annotation.GetMapping;// 导入Spring的GetMapping注解
import org.springframework.web.bind.annotation.PathVariable;// 导入Spring的PathVariable注解
import org.springframework.web.bind.annotation.PostMapping;// 导入Spring的PostMapping注解
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.annotation.IgnoreAuth;// 导入自定义的IgnoreAuth注解
import com.baomidou.mybatisplus.mapper.EntityWrapper;// 导入MyBatis Plus的EntityWrapper类
import com.entity.UsersEntity;// 导入UsersEntity实体类
import com.service.TokenService;// 导入TokenService服务
import com.utils.MPUtil;// 导入TokenService服务ls;
import com.utils.PageUtils;// 导入PageUtils工具类
import com.utils.R; // 导入R工具类

/**
 * 登录相关
 */
@RequestMapping("users") // 定义类级别的请求映射路径
@RestController// 声明这是一个REST控制器
public class UsersController {
	
	@Autowired// 自动注入UsersService服务
	private UsersService usersService;
	
	@Autowired
	private TokenService tokenService;

	/**
	 * 登录
	 */
	@IgnoreAuth// 应用IgnoreAuth注解，表示该接口不需要认证
	@PostMapping(value = "/login")// 定义POST请求映射路径
	public R login(String username, String password, String captcha, HttpServletRequest request) {
		UsersEntity user = usersService.selectOne(new EntityWrapper<UsersEntity>().eq("username", username));
		// 根据用户名查询用户
		if(user==null || !user.getPassword().equals(password)) {// 如果用户不存在或密码不匹配
			return R.error("账号或密码不正确");// 返回错误信息
		}
		String token = tokenService.generateToken(user.getId(),username, "users", user.getRole());// 生成Token
		R r = R.ok();// 创建成功响应对象
		r.put("token", token);// 放入Token
		r.put("role",user.getRole());// 放入角色
		r.put("userId",user.getId());// 放入用户ID
		return r; // 返回响应对象
	}
	
	/**
	 * 注册
	 */
	@IgnoreAuth// 应用IgnoreAuth注解，表示该接口不需要认证
	@PostMapping(value = "/register")// 定义POST请求映射路径
	public R register(@RequestBody UsersEntity user){// 使用RequestBody注解接收请求体
//    	ValidatorUtils.validateEntity(user);
    	if(usersService.selectOne(new EntityWrapper<UsersEntity>().eq("username", user.getUsername())) !=null) {// 如果用户已存在
    		return R.error("用户已存在");// 返回错误信息
    	}
        usersService.insert(user);// 插入用户
        return R.ok();// 返回成功信息
    }

	/**
	 * 退出
	 */
	@GetMapping(value = "logout") // 定义GET请求映射路径
	public R logout(HttpServletRequest request) {// 使用HttpServletRequest参数
		request.getSession().invalidate();// 使Session失效，实现退出
		return R.ok("退出成功"); // 返回成功信息
	}
	
	/**
     * 密码重置
     */
    @IgnoreAuth// 应用IgnoreAuth注解，表示该接口不需要认证
	@RequestMapping(value = "/resetPass")// 定义请求映射路径
    public R resetPass(String username, HttpServletRequest request){// 使用HttpServletRequest参数
    	UsersEntity user = usersService.selectOne(new EntityWrapper<UsersEntity>().eq("username", username));
		// 根据用户名查询用户
		if(user==null) { // 如果用户不存在
    		return R.error("账号不存在");// 返回错误信息
    	}
    	user.setPassword("123456");// 重置密码
        usersService.update(user,null);// 更新用户信息
        return R.ok("密码已重置为：123456");// 返回成功信息
    }
	
	/**
     * 列表
     */
    @RequestMapping("/page")// 定义请求映射路径
    public R page(@RequestParam Map<String, Object> params,UsersEntity user){// 使用RequestParam注解接收请求参数
        EntityWrapper<UsersEntity> ew = new EntityWrapper<UsersEntity>();// 创建EntityWrapper对象
    	PageUtils page = usersService.queryPage(params, MPUtil.sort(MPUtil.between(MPUtil.allLike(ew, user), params), params));// 查询分页数据
        return R.ok().put("data", page);// 返回分页数据
    }

	/**
     * 列表
     */
    @RequestMapping("/list")// 定义请求映射路径
    public R list( UsersEntity user){// 使用UsersEntity参数
       	EntityWrapper<UsersEntity> ew = new EntityWrapper<UsersEntity>();// 创建EntityWrapper对象
      	ew.allEq(MPUtil.allEQMapPre( user, "user")); // 设置查询条件
        return R.ok().put("data", usersService.selectListView(ew));// 返回用户列表视图数据
    }

    /**
     * 信息
     */
    @RequestMapping("/info/{id}")// 定义请求映射路径，包含{id}作为路径变量
    public R info(@PathVariable("id") String id){// 使用PathVariable注解接收路径变量
        UsersEntity user = usersService.selectById(id);// 根据ID查询用户
        return R.ok().put("data", user);// 返回用户信息
    }
    
    /**
     * 获取用户的session用户信息
     */
    @RequestMapping("/session")// 定义请求映射路径
    public R getCurrUser(HttpServletRequest request){// 使用HttpServletRequest参数
    	Integer id = (Integer)request.getSession().getAttribute("userId");// 从Session中获取用户ID
        UsersEntity user = usersService.selectById(id);// 根据ID查询用户
        return R.ok().put("data", user);// 返回当前用户信息
    }

    /**
     * 保存
     */
    @PostMapping("/save")// 定义POST请求映射路径
    public R save(@RequestBody UsersEntity user){// 使用RequestBody注解接收请求体
//    	ValidatorUtils.validateEntity(user);
    	if(usersService.selectOne(new EntityWrapper<UsersEntity>().eq("username", user.getUsername())) !=null) {// 如果用户已存在
    		return R.error("用户已存在"); // 返回错误信息
    	}
    	user.setPassword("123456");// 设置默认密码
        usersService.insert(user);// 插入用户
        return R.ok();// 返回成功信息
    }

    /**
     * 修改
     */
    @RequestMapping("/update")// 定义请求映射路径
    public R update(@RequestBody UsersEntity user){// 使用RequestBody注解接收请求体
//        ValidatorUtils.validateEntity(user);
        usersService.updateById(user);//全部更新
		return R.ok(); // 返回成功信息
    }

    /**
     * 删除
     */
    @RequestMapping("/delete")// 定义请求映射路径
    public R delete(@RequestBody Long[] ids){// 使用RequestBody注解接收请求体
        usersService.deleteBatchIds(Arrays.asList(ids));
        return R.ok();// 返回成功信息
    }
}
