package com.example.demo.finalproject;

import java.util.List;

import org.springframework.data.mongodb.repository.MongoRepository;

public interface FlowdataRepository extends MongoRepository <Flowdata, String>{
	List<Flowdata> findByEmail(String email);
	List<Flowdata> deleteAllByEmail(String email);
}
