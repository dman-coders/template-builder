from . import BaseProject


class Rails(BaseProject):

    @property
    def update(self):
        return super(Rails, self).update + [
            # Force a new install of Rails, over the old copy, to get any updated files.
            'rails new {0} --force'.format(self.builddir)
        ]

    @property
    def platformify(self):
        return super(Rails, self).platformify + [
            'cd {0} && bundle add unicorn pg platform_sh_rails --group "production" --skip-install'.format(self.builddir),
            'cd {0} && echo config/database.yml >> .gitignore'.format(self.builddir),
            'cd {0} && mv config/database.yml config/database.yml.example'.format(self.builddir),
            # Remove the Rails Ruby version lock file, as it's not needed.
            'cd {0} && rm .ruby-version'.format(self.builddir),
            # Remove the Ruby version from the Gemfile, as it pins to a .z release which is too strict.
            "cd {0} && sed '/^ruby /d' Gemfile > temp && mv temp Gemfile".format(self.builddir),
        ]
