package com.example.web;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.apache.struts.action.Action;
import org.apache.struts.action.ActionErrors;
import org.apache.struts.action.ActionForm;
import org.apache.struts.action.ActionForward;
import org.apache.struts.action.ActionMapping;
import org.apache.struts.action.ActionMessage;
import org.apache.struts.validator.DynaValidatorForm;

import org.apache.log4j.Logger;

public class LoginAction extends Action {
    private static final Logger logger = Logger.getLogger(LoginAction.class);

    @Override
    public ActionForward execute(ActionMapping mapping, ActionForm form, 
                                 HttpServletRequest request, HttpServletResponse response)
                                 throws Exception {
        DynaValidatorForm loginForm = (DynaValidatorForm)form;
        String userId = (String)loginForm.get("userId");
        String password = (String)loginForm.get("password");

        logger.info("userId=" + userId + ";");
        logger.info("password=" + password + ";");

        if (!this.certify(userId, password)) {
            logger.info("Failed to certificate;");

            ActionErrors errors = new ActionErrors();
            errors.add("userId", new ActionMessage("login.error"));
            saveErrors(request, errors);
            return mapping.findForward("failure");
        }

        logger.info("Success to certificate;");
        return mapping.findForward("success");
    }

    protected boolean certify(String userId, String password) {
        return ("admin".equals(userId) && "admin".equals(password));
    }
}
