package com.example.bathhack1;

import android.os.Bundle;
import android.webkit.WebView;
import android.webkit.WebViewClient;

import androidx.appcompat.app.AppCompatActivity;

public class Main extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceBundle) {
        super.onCreate(savedInstanceBundle);
        setContentView(R.layout.main_activity);

        WebView myWebView = new WebView(Main.this);
        myWebView.setWebViewClient(new WebViewClient());
        myWebView.loadUrl("https://www.google.com");
        setContentView(myWebView);
    }
}
