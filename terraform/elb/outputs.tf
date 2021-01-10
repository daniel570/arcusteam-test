output "elb_address" {
  value = aws_elb.web.dns_name
}

output "instance1-ip" {
 value = aws_instance.web.public_ip
}

output "instance2-ip" {
 value = aws_instance.web2.public_ip
}
