package com.example.web;

import org.apache.struts.action.Action;
import org.apache.struts.action.ActionForm;
import org.apache.struts.action.ActionForward;
import org.apache.struts.action.ActionMapping;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.apache.log4j.Logger;

public class ProfileAction extends Action {
    private static final Logger logger = Logger.getLogger(ProfileAction.class);

    @Override
    public ActionForward execute(ActionMapping mapping, ActionForm form,
                                 HttpServletRequest request, HttpServletResponse response) throws Exception {
        logger.info("入力が正常なので、welcome.jsp にリダイレクトします。");
        return mapping.findForward("success");
    }
}
