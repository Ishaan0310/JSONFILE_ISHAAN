package com.example.demo.finalproject;

import org.springframework.data.annotation.Id;

import lombok.Data;

@Data
public class Flowdata {
	@Id
	public String _id;

	private String payload;
	private String email;
	private String flowname;
	private String creationinfo;
	private String updationinfo;
}
