package com.example.ptadminer.result;

/**
 * @Projection: ptadminer
 * @Class: Result
 * @Author: Linting 15019763969
 * @Date: 18:03 2022/7/17
 * @Description: TODO
 */
public class Result {
    //响应码
    private int code;

    public Result(int code) {
        this.code = code;
    }

    public int getCode() {
        return code;
    }

    public void setCode(int code) {
        this.code = code;
    }

}
