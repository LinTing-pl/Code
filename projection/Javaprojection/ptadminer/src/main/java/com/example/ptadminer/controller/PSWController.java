package com.example.ptadminer.controller;

import com.example.ptadminer.pojo.PSW;

import com.example.ptadminer.service.PSWService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

/**
 * @Projection: ptadminer
 * @Class: PSWController
 * @Author: Linting 15019763969
 * @Date: 21:14 2022/7/20
 * @Description: TODO
 */
@RestController
public class PSWController {
    @Autowired
    PSWService pswService;

    @CrossOrigin
    @PostMapping("/dev-api/users/psw")
    public void addPsw(@RequestBody PSW psw) throws Exception {
        pswService.add(psw);
    }
}
