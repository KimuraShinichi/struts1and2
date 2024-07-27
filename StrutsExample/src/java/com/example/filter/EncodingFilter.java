package com.example.filter;

import java.io.IOException;
import javax.servlet.Filter;
import javax.servlet.FilterChain;
import javax.servlet.FilterConfig;
import javax.servlet.ServletException;
import javax.servlet.ServletRequest;
import javax.servlet.ServletResponse;

public class EncodingFilter implements Filter {
    public void init(FilterConfig config) throws ServletException {
        // フィルタの初期化処理（必要に応じて）
    }

    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain)
            throws IOException, ServletException {
        // リクエストとレスポンスのエンコーディングをUTF-8に設定
        request.setCharacterEncoding("UTF-8");
        response.setCharacterEncoding("UTF-8");
        chain.doFilter(request, response);
    }

    public void destroy() {
        // フィルタの破棄処理（必要に応じて）
    }
}
