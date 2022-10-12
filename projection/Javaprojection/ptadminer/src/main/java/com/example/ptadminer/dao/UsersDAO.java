package com.example.ptadminer.dao;
import com.example.ptadminer.pojo.Users;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

/**
 * @Projection: ptadminer
 * @Class: UsersDAO
 * @Author: Linting 15019763969
 * @Date: 18:03 2022/7/18
 * @Description: TODO
 */
public interface UsersDAO extends JpaRepository<Users, Integer> {
    Users getById(Integer id);
    List<Users> findByUsernameLikeOrIdentityLikeOrEmailLikeOrPhonenumberLike(String username,String identity,String email,String phonenumber);
}
