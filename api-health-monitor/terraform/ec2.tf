data "aws_ami" "amazon_linux" {
  most_recent = true
  owners      = ["amazon"]

  filter {
    name   = "name"
    values = ["amzn2-ami-hvm-*-x86_64-gp2"]
  }
}

resource "aws_instance" "monitor" {
  ami                  = data.aws_ami.amazon_linux.id
  instance_type        = var.instance_type
  iam_instance_profile = aws_iam_instance_profile.profile.name

  user_data = <<EOF
#!/bin/bash
yum update -y
yum install -y python3 git
pip3 install boto3 requests

mkdir -p /app
cd /app

export CONFIG_TABLE=api_config
export STATE_TABLE=api_state
export SNS_TOPIC_ARN=${aws_sns_topic.alerts.arn}
EOF

  tags = {
    Name = "api-health-monitor"
  }
}

