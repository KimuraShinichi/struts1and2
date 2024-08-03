package com.example.web.action;

import com.opensymphony.xwork2.ActionSupport;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

public class LoginAction extends ActionSupport {
    private static final Logger logger = LogManager.getLogger(LoginAction.class);

    private String userId;
    private String password;

    public String getUserId() { return this.userId; }
    public void setUserId(String userId) { this.userId = userId; }

    public String getPassword() { return this.password; }
    public void setPassword(String password) { this.password = password; }

    @Override
    public String execute() {
        logger.info("userId=" + userId + ";");
        logger.info("password=" + password + ";");

        if (!this.certify(userId, password)) {
            logger.info("Failed to certificate;");

            addFieldError("userId", getText("login.error"));
            return ActionSupport.INPUT;
        }

        logger.info("Success to certificate;");
        return ActionSupport.SUCCESS;
    }

    protected boolean certify(String userId, String password) {
        return ("admin".equals(userId) && "admin".equals(password));
    }
}
