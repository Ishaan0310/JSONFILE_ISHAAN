package com.example.demo.finalproject;

import java.util.List;

import javax.validation.Valid;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

@CrossOrigin
@RestController
public class FlowdataController {
	
	@Autowired
	private FlowdataRepository flowdataRepo;
	
	@PostMapping("/getflows")
	public List<Flowdata> getFlows(@Valid @RequestBody Getflowdata newflows) 
	{
		List<Flowdata> flows = flowdataRepo.findByEmail(newflows.getEmail());
		return flows;
	}
	
	@PostMapping("/postflows")
	public Flowdata updateFlows(@Valid @RequestBody Flowdata newflows)
	{ 
    		return flowdataRepo.save(newflows);
    }
	
	@PutMapping("/putflows/{id}")
	public Flowdata putFlows(@Valid @RequestBody Editflowdata payload, @PathVariable String id)
	{
		Flowdata flowsindb = flowdataRepo.findById(id).get();
		flowsindb.setPayload(payload.getPayload());
		flowsindb.setUpdationinfo(payload.getUpdationinfo());
		flowsindb.setFlowname(payload.getFlowname());
		return flowdataRepo.save(flowsindb);
    }
	
	@DeleteMapping("/deleteflow/{id}")
	public void deleteflowbyid(@PathVariable String id)
	{
		flowdataRepo.deleteById(id);
	}
	
	@DeleteMapping("/deleteallflows/{email}")
	public void deleteallflowsbyemail(@PathVariable String email)
	{
		flowdataRepo.deleteAllByEmail(email);
	}
}
