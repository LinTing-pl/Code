package com.example.ptadminer.service;

import com.example.ptadminer.dao.PSWDAO;
import com.example.ptadminer.pojo.PSW;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

/**
 * @Projection: ptadminer
 * @Class: PSWService
 * @Author: Linting 15019763969
 * @Date: 21:09 2022/7/20
 * @Description: TODO
 */
@Service
public class PSWService {
    @Autowired
    public PSWDAO pswDAO;

    public void add(PSW psw) {
        pswDAO.save(psw);
    }
}
