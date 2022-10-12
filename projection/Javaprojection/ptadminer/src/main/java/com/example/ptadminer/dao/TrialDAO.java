package com.example.ptadminer.dao;


import com.example.ptadminer.pojo.Trial;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

/**
 * @Projection: ptadminer
 * @Class: JobDAO
 * @Author: Linting 15019763969
 * @Date: 14:30 2022/7/23
 * @Description: TODO
 */
public interface TrialDAO extends JpaRepository<Trial, Integer> {
    Trial getById(Integer id);

    List<Trial> findByTrialEqualsAndJobLikeOrTrialEqualsAndPhonenumberLikeOrTrialEqualsAndCityLikeOrTrialEqualsAndContentLikeOrTrialEqualsAndAdressLikeOrTrialEqualsAndBeifenLike(String o, String job, String oo, String phonenumber, String ooo, String city, String oooo, String content, String ooooo, String adress, String oooooo, String beifen);

    List<Trial> findByCid(String cid);

    List<Trial> findByTrial(String trial);
}
