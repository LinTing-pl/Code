package com.example.ptadminer.dao;
import com.example.ptadminer.pojo.Launch;
import org.springframework.data.jpa.repository.JpaRepository;

/**
 * @Projection: ptadminer
 * @Class: UsersDAO
 * @Author: Linting 15019763969
 * @Date: 18:03 2022/7/18
 * @Description: TODO
 */
public interface LaunchDAO extends JpaRepository<Launch, Integer> {
    Launch getById(Integer id);
}
