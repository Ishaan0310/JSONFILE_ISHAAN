package com.example.demo.finalproject;

import lombok.Data;

@Data
public class Token {
	
	private String token;
	private String type="Bearer";
	private Long id;
	private String email;
	private String firstname;
	private String lastname;

}
