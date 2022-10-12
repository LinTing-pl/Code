package com.example.ptadminer.controller;


import com.example.ptadminer.pojo.Launch;
import com.example.ptadminer.service.LaunchService;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
public class LaunchController {
    @Autowired
    LaunchService launchService;

    @CrossOrigin
    @GetMapping("/dev-api/powers/get")
    public List<Launch> list() throws Exception {
        return launchService.list();
    }

    @CrossOrigin
    @PostMapping("/dev-api/powers/add")
    public void add(@RequestBody Launch launch) throws Exception {
        launchService.add(launch);
    }

    @CrossOrigin
    @PostMapping("/dev-api/powers/update")
    public void update(@RequestBody Launch launch) throws Exception {
        launchService.update(launch);
    }

    @CrossOrigin
    @DeleteMapping("/dev-api/powers/delete/{id}")
    public void delete(@PathVariable("id") String id) {
        launchService.deleteById(Integer.parseInt(id));
    }
}


