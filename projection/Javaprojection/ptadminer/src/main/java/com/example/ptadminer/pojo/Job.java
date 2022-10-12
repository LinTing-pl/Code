package com.example.ptadminer.pojo;

/**
 * @Projection: ptadminer
 * @Class: Job
 * @Author: Linting 15019763969
 * @Date: 14:31 2022/7/23
 * @Description: TODO
 */

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;

import javax.persistence.*;

@Entity
@Table(name = "parttimejob")
@JsonIgnoreProperties({"handler", "hibernateLazyInitializer"})

public class Job {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id")
    int id;


    String username;
    String job;
    String phonenumber;
    String city;
    String content;
    String adress;
    String beifen;
    String cid;
    String keysort;
    String toptrial;

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public String getJob() {
        return job;
    }

    public void setJob(String job) {
        this.job = job;
    }

    public String getPhonenumber() {
        return phonenumber;
    }

    public void setPhonenumber(String phonenumber) {
        this.phonenumber = phonenumber;
    }

    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }

    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }

    public String getAdress() {
        return adress;
    }

    public void setAdress(String adress) {
        this.adress = adress;
    }

    public String getBeifen() {
        return beifen;
    }

    public void setBeifen(String beifen) {
        this.beifen = beifen;
    }

    public String getCid() {
        return cid;
    }

    public void setCid(String cid) {
        this.cid = cid;
    }

    public String getKeysort() {
        return keysort;
    }

    public void setKeysort(String keysort) {
        this.keysort = keysort;
    }

    public String getToptrial() {
        return toptrial;
    }

    public void setToptrial(String toptrial) {
        this.toptrial = toptrial;
    }
}
