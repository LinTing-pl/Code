package com.example.ptadminer.controller;

import com.example.ptadminer.pojo.Users;
import com.example.ptadminer.service.UsersService;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
public class UsersController {
    @Autowired
    UsersService usersService;

    @CrossOrigin
    @GetMapping("/dev-api/users/get")
    public List<Users> list() throws Exception {
        return usersService.list();
    }

    @CrossOrigin
    @GetMapping("/dev-api/users/search/{search}")
    public List<Users> search(@PathVariable String search) throws Exception {
        System.out.println(search);
        return usersService.search(search);
    }

    @CrossOrigin
    @PostMapping("/dev-api/users/post")
    public Users add(@RequestBody Users users) throws Exception {
        usersService.add(users);
        return users;
    }

    @CrossOrigin
    @PostMapping("/dev-api/users/update")
    public Users update(@RequestBody Users users) throws Exception {
        usersService.update(users);
        return users;
    }


    @CrossOrigin
    @DeleteMapping("/dev-api/users/delete/{id}")
    public void delete(@PathVariable("id") String id) throws Exception {
        System.out.println(id);
        usersService.deleteById(Integer.parseInt(id));
    }
}


