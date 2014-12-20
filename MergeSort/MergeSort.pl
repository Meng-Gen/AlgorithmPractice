use strict;
use warnings;

sub merge_sort {
    my @array = @_;
    return @array if @array < 2;

    my $median = int @array / 2;
    my @left = merge_sort(@array[0 .. $median - 1]);
    my @right = merge_sort(@array[$median .. $#array]);
    for (@array) {
        $_ = !@left                ? shift @right
           : !@right               ? shift @left
           : $left[0] <= $right[0] ? shift @left
           :                         shift @right
           ;
    }
    return @array;
}

sub main {
    my @array = (4, 65, 2, -31, 0, 99, 83, 782, 1);
    @array = merge_sort(@array);
    print "@array\n";
}

unless (caller) {
    main();
}
