package com.example.web;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import org.apache.struts.action.Action;
import org.apache.struts.action.ActionForm;
import org.apache.struts.action.ActionForward;
import org.apache.struts.action.ActionMapping;

public class HelloWorldAction extends Action {
    @Override
    public ActionForward execute(ActionMapping mapping, ActionForm form, 
                                 HttpServletRequest request, HttpServletResponse response) {
        return mapping.findForward("success");
    }
}
