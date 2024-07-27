package com.example.web.action;

import com.opensymphony.xwork2.ActionSupport;

public class HelloWorldAction extends ActionSupport {
    private String message;

    public String execute() {
        setMessage("Hello, World!");
        return "success";
    }

    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
}
