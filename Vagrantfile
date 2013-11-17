Vagrant.configure("2") do |config|
    config.vm.define "staging" do |staging|
        staging.vm.box = "precise32"
    #   staging.vm.provision :shell, :path => "bootstrap.sh"
        staging.vm.network :forwarded_port, host: 8888, guest: 80
    end
end
