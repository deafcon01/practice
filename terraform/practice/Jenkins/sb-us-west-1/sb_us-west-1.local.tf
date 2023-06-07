locals {
    // Common Tags
    tags = {
        Owner = "SPH"
        Environment = "sandbox"
        CostCenter = "4847"
    }

    ingress_ports = [
        {
            from_port = 32222
            to_port = 32225
            protocol = -1
            description = "test ports"
        }
    ]
}