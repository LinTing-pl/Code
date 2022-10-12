package com.example.ptadminer.service;

import com.example.ptadminer.pojo.Job;
import com.example.ptadminer.dao.JobDAO;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Sort;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class JobService {
    @Autowired
    public JobDAO jobDAO;

    public List<Job> list() {
        return jobDAO.findAllByOrderByKeysortDescIdDesc();
    }
    public List<Job> listTop() {
        return jobDAO.findByToptrial("1");
    }

    public void add(Job job) {
        jobDAO.save(job);
    }

    public void update(Job job) {
        jobDAO.save(job);
    }

    public void deleteById(Integer id) {
        jobDAO.deleteById(id);
    }

    public List<Job> search(String search) {

        return jobDAO.findByJobLikeOrPhonenumberLikeOrCityLikeOrContentLikeOrAdressLikeOrBeifenLike("%" + search + "%", "%" + search + "%", "%" + search + "%", "%" + search + "%", "%" + search + "%", "%" + search + "%");
    }
}
