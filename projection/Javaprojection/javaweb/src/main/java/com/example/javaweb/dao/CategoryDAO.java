package com.example.javaweb.dao;

import org.springframework.data.jpa.repository.JpaRepository;

import com.example.javaweb.pojo.Category;

public interface CategoryDAO extends JpaRepository<Category, Integer> {

}

