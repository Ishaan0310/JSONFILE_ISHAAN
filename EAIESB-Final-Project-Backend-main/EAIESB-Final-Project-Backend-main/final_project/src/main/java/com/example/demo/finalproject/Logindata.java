package com.example.demo.finalproject;

import org.springframework.data.annotation.Id;

import lombok.Data;

@Data
public class Logindata {

	@Id
	public String _id;

	private String email;
	private String password;
}
