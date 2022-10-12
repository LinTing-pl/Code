package com.example.ptadminer.controller;


import com.example.ptadminer.pojo.Job;
import com.example.ptadminer.service.JobService;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
public class JobController {
    @Autowired
    JobService jobService;

    @CrossOrigin
    @GetMapping("/dev-api/job/get")
    public List<Job> list() throws Exception {
        return jobService.list();
    }
    @CrossOrigin
    @GetMapping("/dev-api/job/gettop1")
    public List<Job> listTop() throws Exception {
        return jobService.listTop();
    }

    @CrossOrigin
    @PostMapping("/dev-api/job/add")
    public void add(@RequestBody Job job) throws Exception {
        jobService.add(job);
    }

    @CrossOrigin
    @PostMapping("/dev-api/job/update")
    public void update(@RequestBody Job job) throws Exception {
        jobService.update(job);
    }
    @CrossOrigin
    @PostMapping("/dev-api/job/updatetop")
    public void updateTop(@RequestBody Job job) throws Exception {
        jobService.update(job);
    }

    @CrossOrigin
    @DeleteMapping("/dev-api/job/delete/{id}")
    public void delete(@PathVariable("id") String id) {
        jobService.deleteById(Integer.parseInt(id));
    }

    @CrossOrigin
    @GetMapping("/dev-api/job/get/{search}")
    public List<Job> search(@PathVariable("search") String search) {
        return jobService.search(search);
    }

    @CrossOrigin
    @PostMapping("/dev-api/job/trial")
    public void trial(Job job) {
        jobService.add(job);
    }
}



