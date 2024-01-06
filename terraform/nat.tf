resource "aws_eip" "elastic_ip" {
  domain = "vpc"
  tags = {
    Name = "${var.service_name}-elastic-ip"
  }
}
resource "aws_nat_gateway" "nat_gateway" {
  allocation_id = aws_eip.elastic_ip.id
  subnet_id     = aws_subnet.public.id

  tags = {
    Name = "${var.service_name}-natgw"
  }
}
