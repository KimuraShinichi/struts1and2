package com.example.web;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.apache.struts.action.Action;
import org.apache.struts.action.ActionForm;
import org.apache.struts.action.ActionForward;
import org.apache.struts.action.ActionMapping;
import org.apache.struts.action.ActionMessages;
import org.apache.struts.action.ActionMessage;

public class ShowErrorSampleAction extends Action {
    @Override
    public ActionForward execute(ActionMapping mapping, ActionForm form, HttpServletRequest request, HttpServletResponse response) {

        // エラーメッセージの設定
        ActionMessages errors = new ActionMessages();
        errors.add(ActionMessages.GLOBAL_MESSAGE, new ActionMessage("message.error"));
        saveErrors(request, errors);

        // エラーページにフォワード
        return mapping.findForward("error");
    }
}
