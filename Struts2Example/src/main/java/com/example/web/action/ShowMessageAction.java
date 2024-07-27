package com.example.web.action;

import com.opensymphony.xwork2.ActionSupport;

public class ShowMessageAction extends ActionSupport {
    @Override
    public String execute() {
        // 成功メッセージの設定
        addActionMessage(getText("message.success"));
        // エラーメッセージの設定
        addActionError(getText("message.error"));
        return SUCCESS;
    }
}
