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

public class LoginAction extends Action {

    @Override
    public ActionForward execute(ActionMapping mapping, ActionForm form, 
                                 HttpServletRequest request, HttpServletResponse response)
                                 throws Exception {
        DynaValidatorForm loginForm = (DynaValidatorForm)form;
        String username = (String)loginForm.get("username");
        String password = (String)loginForm.get("password");

        ActionErrors errors = new ActionErrors();

        // Sample logic for authentication
        if ("admin".equals(username) && "admin".equals(password)) {
            return mapping.findForward("success");
        } else {
            errors.add("username", new ActionMessage("error.username.invalid"));
            saveErrors(request, errors);
            return mapping.findForward("failure");
        }
    }
}
