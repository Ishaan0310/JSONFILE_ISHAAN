package com.example.demo.finalproject;

import java.util.List;
import java.util.Optional;

import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;

public interface UserdataRepository extends MongoRepository <Userdata, String>{

	Userdata findByEmail(String email);
	Userdata deleteByEmail(String email);

}
