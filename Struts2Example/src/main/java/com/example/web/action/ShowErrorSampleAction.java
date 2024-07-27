package com.example.web.action;

import com.opensymphony.xwork2.ActionSupport;

public class ShowErrorSampleAction extends ActionSupport {
    @Override
    public String execute() {
        // エラーメッセージの設定
        addActionError(getText("message.error"));
        return ERROR;
    }
}
