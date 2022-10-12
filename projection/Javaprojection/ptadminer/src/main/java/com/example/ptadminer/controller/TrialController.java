package com.example.ptadminer.controller;

import com.example.ptadminer.pojo.Trial;
import com.example.ptadminer.service.TrialService;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
public class TrialController {
    @Autowired
    TrialService trialService;

    @CrossOrigin
    @GetMapping("/dev-api/trial/get1")
    public List<Trial> list1() throws Exception {
        return trialService.list1();
    }

    @CrossOrigin
    @PostMapping("/dev-api/trial/add")
    public void add(@RequestBody Trial trial) throws Exception {
        trialService.add(trial);
    }

    @CrossOrigin
    @PostMapping("/dev-api/trial/update")
    public void update(@RequestBody Trial trial) throws Exception {
        trialService.update(trial);
    }

    @CrossOrigin
    @DeleteMapping("/dev-api/trial/delete/{id}")
    public void delete(@PathVariable("id") String id) {
        trialService.deleteById(Integer.parseInt(id));
    }

}




