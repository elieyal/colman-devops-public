# Data sources Block
# Get latest AMI ID for Amazon Linux2 OS
data "aws_ami" "amzlinux" {
  most_recent  	= true
  owners       	= ["amazon"]

  filter {
	name   = "name"
	values = ["al2023-ami-2023.*-kernel-*"]
  }

  filter {
	name   = "root-device-type"
	values = ["ebs"]
  }

  filter {
	name   = "virtualization-type"
	values = ["hvm"]
  }

  filter {
	name   = "architecture"
	values = ["x86_64"]
  }
}

# Resource Block
resource "aws_instance" "web_server" {
  ami                         = data.aws_ami.amzlinux.id
  instance_type               = "t2.micro"
  subnet_id                   = module.vpc.public_subnets[0]
  vpc_security_group_ids      = [aws_security_group.web_servers.id]
  associate_public_ip_address = true
  key_name                    = local.keypair

  user_data = file("init.sh")

  root_block_device {
    volume_size = 8
    volume_type = "gp3"
  }

  tags = merge(
    local.common_tags,
    {
      Name = "web-server"
    }
  )
}