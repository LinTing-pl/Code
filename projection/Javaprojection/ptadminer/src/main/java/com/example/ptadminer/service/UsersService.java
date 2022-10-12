package com.example.ptadminer.service;

import com.example.ptadminer.dao.UsersDAO;
import com.example.ptadminer.pojo.Users;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Sort;
import org.springframework.stereotype.Service;
import java.util.List;

@Service
public class UsersService {
    @Autowired
    public UsersDAO usersDAO;

    public Users get(Integer id) {
        return usersDAO.getById(id);
    }

    public List<Users> list() {
        Sort sort = Sort.by(Sort.Direction.DESC, "id");
        return usersDAO.findAll(sort);
    }


    public List<Users> search(String search) {
        return usersDAO.findByUsernameLikeOrIdentityLikeOrEmailLikeOrPhonenumberLike("%"+search+"%","%"+search+"%","%"+search+"%","%"+search+"%");
    }

    public void add(Users users) {
        usersDAO.save(users);
    }

    public void update(Users users) {
        Users u = get(users.getId());
        u.setEmail(users.getEmail());
        u.setPhonenumber(users.getPhonenumber());
        usersDAO.save(u);
    }

    ;

    public void deleteById(int id) {
        usersDAO.deleteById(id);
    }
}

