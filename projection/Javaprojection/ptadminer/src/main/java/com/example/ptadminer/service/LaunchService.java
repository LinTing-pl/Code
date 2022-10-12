package com.example.ptadminer.service;

import com.example.ptadminer.dao.LaunchDAO;
import com.example.ptadminer.pojo.Launch;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Sort;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class LaunchService {
    @Autowired
    public LaunchDAO launchDAO;

    public List<Launch> list() {
        Sort sort = Sort.by(Sort.Direction.DESC, "id");
        return launchDAO.findAll(sort);
    }

    public void add(Launch launch) {
        launchDAO.save(launch);
    }
    public void update(Launch launch){
        launchDAO.save(launch);
    }
    public void deleteById(Integer id) {
        launchDAO.deleteById(id);
    }
}


