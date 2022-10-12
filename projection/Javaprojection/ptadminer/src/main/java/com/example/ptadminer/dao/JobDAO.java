package com.example.ptadminer.dao;

import com.example.ptadminer.pojo.Job;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

/**
 * @Projection: ptadminer
 * @Class: JobDAO
 * @Author: Linting 15019763969
 * @Date: 14:30 2022/7/23
 * @Description: TODO
 */
public interface JobDAO extends JpaRepository<Job, Integer> {
    Job getById(Integer id);

    List<Job> findByJobLikeOrPhonenumberLikeOrCityLikeOrContentLikeOrAdressLikeOrBeifenLike(String job, String phonenumber, String city, String content, String adress, String beifen);
    List<Job> findAllByOrderByKeysortDescIdDesc();
    List<Job> findByToptrial(String trial);
}
