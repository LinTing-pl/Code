package com.example.ptadminer.service;

import com.example.ptadminer.pojo.Trial;
import com.example.ptadminer.dao.TrialDAO;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Sort;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class TrialService {
    @Autowired
    public TrialDAO trialDAO;

    public List<Trial> list1() {
        return trialDAO.findByTrial("1");
    }

    public List<Trial> listByCid(String cid) {
        return trialDAO.findByCid(cid);
    }

    public void add(Trial trial) {
        trialDAO.save(trial);
    }

    public void update(Trial trial) {
        trialDAO.save(trial);
    }

    public void deleteById(Integer id) {
        trialDAO.deleteById(id);
    }
}
